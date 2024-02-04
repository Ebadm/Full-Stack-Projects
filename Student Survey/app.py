from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

# Connect to the database
def connect_db():
    return sqlite3.connect('database.db')

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        email = request.form['email']
        course_code = request.form['course_code']
        answers = {}
        for key in request.form.keys():
            if key.startswith("question_"):
                question_id = int(key.split("_")[1])
                answer_value = int(request.form[key])
                answers[question_id] = answer_value

        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT survey_id FROM Survey WHERE email=? AND course_code=?', (email, course_code))
            survey_id = cursor.fetchone()

            if survey_id:
                flash('You have already answered this survey!', 'error')
            else:
                cursor.execute('INSERT INTO Survey (email, course_code) VALUES (?, ?)', (email, course_code))
                conn.commit()
                survey_id = cursor.lastrowid

                for question_id, answer_value in answers.items():
                    cursor.execute('INSERT INTO Answer (survey_id, question_id, answer_value) VALUES (?, ?, ?)',
                                   (survey_id, question_id, answer_value))
                conn.commit()
                flash('Thank you for submitting the survey!', 'success')
                return redirect(url_for('home'))

    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Course')
        courses = cursor.fetchall()
        cursor.execute('SELECT * FROM Question')
        questions = cursor.fetchall()
    return render_template('survey.html', courses=courses, questions=questions)

    
    
@app.route('/results')
def results():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Course')
        courses = cursor.fetchall()
    return render_template('results.html', courses=courses)



@app.route('/results/<course_code>')
def course_results(course_code):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    course = cur.execute('SELECT * FROM Course WHERE course_code = ?', (course_code,)).fetchone()
    questions = cur.execute('SELECT * FROM Question').fetchall()

    question_means = []
    closest_values = []
    for question in questions:
        mean_value = cur.execute('SELECT AVG(answer_value) FROM Answer '
                                 'JOIN Survey ON Answer.survey_id = Survey.survey_id '
                                 'WHERE course_code = ? AND question_id = ?',
                                 (course_code, question[0])).fetchone()[0]
        question_means.append(mean_value)

        closest_value = min([1, 2, 3, 4, 5], key=lambda x: abs(x - mean_value))
        closest_values.append(closest_value)

    answer_key = {
        1: 'Strongly Disagree',
        2: 'Disagree',
        3: 'Neutral',
        4: 'Agree',
        5: 'Strongly Agree'
    }

    closest_texts = [answer_key[value] for value in closest_values]

    results = zip(questions, question_means, closest_texts)

    return render_template('course_results.html', course=course, results=results, answer_key=answer_key)



# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()