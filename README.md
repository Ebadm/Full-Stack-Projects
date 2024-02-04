# Full Stack Web Development Projects

This repository is a compilation of full stack web applications developed using Flask and Django frameworks. The projects showcase backend development skills with robust database integration, including both SQL and SQLite. Each sub-directory represents a unique web application, catering to different use cases such as blogging platforms, chat services, student surveys, and weather reporting.

## Projects Overview

- **Blog**: A blogging platform built with Django, enabling users to create, edit, and view posts.
- **Chat Application**: A real-time chat service developed with Django, facilitating live messaging between users.
- **Student Survey**: A survey platform designed to collect and analyze student feedback, implemented in Flask.
- **Weather Application**: A Django-based application that reports current weather conditions and forecasts.

## Technology Stack

- **Web Frameworks**: Flask, Django
- **Databases**: SQLite, SQL
- **Frontend**: HTML5, CSS3 (Templates included in each app directory)
- **Deployment**: Gunicorn/Nginx (for Django projects), Flask development server for demonstration

## Project Structure

Each application is contained within its own directory, encapsulating its templates, database files, and application code:

- `/Blog`
  - `/templates` - HTML templates for the blog views.
  - `db.sqlite3` - The SQLite database for storing blog posts.
  - `app.py` - The Django application script for the blog.
- `/Chat Application`
  - `/chat` - Django app for the chat functionality.
  - `/templates` - HTML templates for chat interface.
  - `db.sqlite3` - The SQLite database for chat messages.
  - `manage.py` - Django's command-line utility for administrative tasks.
- `/Student Survey`
  - `/Diagrams` - Contains ER and relational diagrams for the survey database.
  - `/Report` - A comprehensive report on the survey application.
  - `/templates` - HTML templates for survey forms and results.
  - `database.db` - SQLite database holding survey data.
  - `database.sql` - SQL script for creating and populating survey tables.
  - `app.py` - The Flask application for the survey platform.
- `/Weather Application`
  - `/weather` - Django app for weather reporting.
  - `/weatherdetector` - Django project settings.
  - `/templates` - HTML templates for displaying weather data.
  - `db.sqlite3` - SQLite database for storing weather records.
  - `manage.py` - Django's command-line utility for administrative tasks.

## Setup and Running Applications

For each project, ensure you have the necessary dependencies installed:

```bash
pip install -r requirements.txt
