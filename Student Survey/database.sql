CREATE TABLE Student (
    email TEXT PRIMARY KEY,
    user_name TEXT NOT NULL
);

CREATE TABLE Course (
    course_code TEXT PRIMARY KEY,
    course_title TEXT NOT NULL
);

CREATE TABLE Survey (
    survey_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_code INTEGER NOT NULL,
    email TEXT NOT NULL,
    FOREIGN KEY (course_code) REFERENCES Course(course_code),
    FOREIGN KEY (email) REFERENCES Student(email)
);

CREATE TABLE Question (
    question_id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_text TEXT NOT NULL
);

CREATE TABLE SurveyQuestion (
    survey_id INTEGER NOT NULL,
    question_id INTEGER NOT NULL,
    PRIMARY KEY (survey_id, question_id),
    FOREIGN KEY (survey_id) REFERENCES Survey(survey_id),
    FOREIGN KEY (question_id) REFERENCES Question(question_id)
);

CREATE TABLE Answer (
    survey_id INTEGER NOT NULL,
    question_id INTEGER NOT NULL,
    answer_value INTEGER NOT NULL,
    answer_text TEXT,
    PRIMARY KEY (survey_id, question_id),
    FOREIGN KEY (survey_id, question_id) REFERENCES SurveyQuestion(survey_id, question_id)
);
------Now, let's populate the database with some initial data:

-- Insert students
INSERT INTO Student (email, user_name) VALUES ('student1@example.com', 'John Doe');
INSERT INTO Student (email, user_name) VALUES ('student2@example.com', 'Jane Smith');

-- Insert courses
INSERT INTO Course (course_code, course_title) VALUES ('EBA3420', 'Databases');
INSERT INTO Course (course_code, course_title) VALUES ('EBA3400', 'Python Programming');

-- Insert questions
INSERT INTO Question (question_text) VALUES ('I have got a clear idea of what is expected of me in this course.');
INSERT INTO Question (question_text) VALUES ('The lecturer(s) in this course presented the course contents well.');
INSERT INTO Question (question_text) VALUES ('The course literature has supported my learning.');
INSERT INTO Question (question_text) VALUES ('I have acquired new and relevant knowledge in the course area.');

--Insert Surveys
INSERT INTO Survey (course_code, email) VALUES ('EBA3420', 'student1@example.com');
INSERT INTO Survey (course_code, email) VALUES ('EBA3400', 'student2@example.com');

-- Insert survey questions for each course
INSERT INTO SurveyQuestion (survey_id, question_id) VALUES
(1, 1), (1, 2), (1, 3), (1, 4),
(2, 1), (2, 2), (2, 3), (2, 4);

-- Insert answer choices
INSERT INTO Answer (survey_id, question_id, answer_value, answer_text) VALUES
(1, 1, 4, 'Agree'),
(1, 2, 5, 'Strongly Agree'),
(1, 3, 3, 'Neutral'),
(1, 4, 4, 'Agree'),
(2, 1, 3, 'Neutral'),
(2, 2, 2, 'Disagree'),
(2, 3, 5, 'Strongly Agree'),
(2, 4, 1, 'Strongly Disagree');