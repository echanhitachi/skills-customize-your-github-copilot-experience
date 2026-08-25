"""Starter code for SQL-Powered Student Gradebook CLI.

Usage examples:
  python starter-code.py init
  python starter-code.py add-student "Ada Lovelace" ada@example.com
  python starter-code.py add-assignment "Quiz 1" 20
  python starter-code.py record-grade 1 1 18
  python starter-code.py student-report 1
  python starter-code.py class-summary
"""

import sqlite3
import sys
from pathlib import Path

DB_PATH = Path("gradebook.db")


def get_connection():
    """Open a SQLite connection."""
    return sqlite3.connect(DB_PATH)


def init_db(conn):
    """Create tables for students, assignments, and grades."""
    # TODO: Create tables with constraints.
    pass


def add_student(conn, name, email):
    """Insert a student row."""
    # TODO: Add INSERT statement and handle duplicate email errors.
    pass


def add_assignment(conn, title, points_possible):
    """Insert an assignment row."""
    # TODO: Add INSERT statement and validate points_possible > 0.
    pass


def record_grade(conn, student_id, assignment_id, points_earned):
    """Insert or update a grade row."""
    # TODO: Validate references and write to grades table.
    pass


def student_report(conn, student_id):
    """Print one student's detailed grade report."""
    # TODO: Use JOIN queries and aggregate totals.
    pass


def class_summary(conn):
    """Print class averages per assignment."""
    # TODO: Use GROUP BY and AVG() for assignment summaries.
    pass


def main(argv):
    if len(argv) < 2:
        print("Usage: python starter-code.py <command> [args...]")
        return

    command = argv[1]
    with get_connection() as conn:
        if command == "init":
            init_db(conn)
            print("Database initialized.")
        elif command == "add-student" and len(argv) == 4:
            add_student(conn, argv[2], argv[3])
            print("Student added.")
        elif command == "add-assignment" and len(argv) == 4:
            add_assignment(conn, argv[2], float(argv[3]))
            print("Assignment added.")
        elif command == "record-grade" and len(argv) == 5:
            record_grade(conn, int(argv[2]), int(argv[3]), float(argv[4]))
            print("Grade recorded.")
        elif command == "student-report" and len(argv) == 3:
            student_report(conn, int(argv[2]))
        elif command == "class-summary":
            class_summary(conn)
        else:
            print("Invalid command or arguments.")


if __name__ == "__main__":
    main(sys.argv)
