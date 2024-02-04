# Campus Pulse: A Comprehensive Student Survey Platform

## Project Overview

In thisproject, we combined comprehensive database management skills with some software engineering. The project involved creating an Entity-Relationship (ER) model based on a specified information system scenario, converting it to a relational model, implementing it in an SQLite database, populating it with data, and developing a web application for querying and modifying the database using Flask.

## Project Structure

The project is organized into several key components:

- **ER Model**: The foundation of our database system, designed to avoid data redundancy and ensure efficient data organization.
- **Relational Model**: Conversion of the ER model into a normalized relational schema, specifically ensuring all tables adhere to the Third Normal Form (3NF).
- **SQLite Database**: Implementation of the database schema using SQLite, chosen for its simplicity and ease of integration with web applications.
- **Web Application**: A Flask-based web application that provides user-friendly interfaces for querying and modifying the database.

## Components

This repository contains all the components and documentation for the project:

- `ER-Diagram.pdf`: The ER diagram visualizing the structure of the database.
- `Relational-Schema.pdf`: A document outlining the relational schema derived from the ER model (optional).
- `Assumptions.md`: Documentation of any assumptions made during the database design process.
- `SQL-Statements.sql`: Contains all SQL Data Definition Language (DDL) and Data Manipulation Language (DML) statements used to create and populate the database.
- `database.db`: The SQLite database file, populated with initial data for testing and demonstration purposes.
- `/app`: The Flask web application source code, including `app.py` and the `/templates` directory with all HTML files.

## Implementation Details

### Database Design

- **ER Model Creation**: Utilized ERDPlus for diagram creation, focusing on capturing all necessary entities, relationships, and attributes based on the project scenario.
- **Relational Schema Conversion**: Manually converted the ER model to a relational schema, ensuring normalization and defining primary and foreign keys accurately.
- **SQLite Database Implementation**: Executed SQL DDL statements to create the database schema and used SQL DML statements for initial data population.

### Web Application Development

- Developed using Flask, the web application provides interfaces for data querying and modification.
- Implements CRUD (Create, Read, Update, Delete) operations on the database.
- Utilizes HTML templates for dynamic data presentation and interaction.

## How to Use

1. Clone the repository to your local machine.
2. Install the necessary Python packages, including Flask and SQLite, using `pip install -r requirements.txt`.
3. Run the Flask application by executing `python app.py`.
4. Access the web application through your browser at `http://localhost:5000`.

## Additional Assumptions

For detailed assumptions made during the database and application design process, refer to `Assumptions.md`.

