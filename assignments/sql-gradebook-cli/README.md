# 📘 Assignment: SQL-Powered Student Gradebook CLI

## 🎯 Objective

Build a command-line gradebook tool that stores data in SQLite and uses SQL queries to add, update, and report student performance.

## 📝 Tasks

### 🛠️	Design the Gradebook Database

#### Description
Create and initialize a SQLite database schema for students, assignments, and grades.

#### Requirements
Completed program should:

- Create a SQLite database file named `gradebook.db` if it does not exist
- Create a `students` table with `id`, `name`, and `email`
- Create an `assignments` table with `id`, `title`, and `points_possible`
- Create a `grades` table with `student_id`, `assignment_id`, and `points_earned`
- Enforce unique student emails and prevent duplicate grade entries for the same student-assignment pair

### 🛠️	Build CLI Commands and Reports

#### Description
Implement command-line actions to manage records and produce summary reports using SQL joins and aggregates.

#### Requirements
Completed program should:

- Support commands: `init`, `add-student`, `add-assignment`, `record-grade`, `student-report`, and `class-summary`
- Validate bad input and print clear error messages instead of crashing
- Use SQL joins to generate each student report with assignment names and scores
- Compute each student percentage and letter grade in the `student-report` output
- Compute class average per assignment in the `class-summary` output
