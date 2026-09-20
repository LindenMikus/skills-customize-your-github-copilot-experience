from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Mergington Student Directory")

students = [
    {
        "name": "Jordan Lee",
        "grade": 10,
        "favorite_subject": "Biology",
    },
    {
        "name": "Sam Rivera",
        "grade": 11,
        "favorite_subject": "Computer Science",
    },
]


class Student(BaseModel):
    """Data required to create a student record."""

    name: str = Field(min_length=1)
    grade: int = Field(ge=9, le=12)
    favorite_subject: str = Field(min_length=1)


@app.get("/students")
def list_students():
    """Return all student records."""
    # TODO: Return the students list.
    pass


@app.post("/students", status_code=201)
def create_student(student: Student):
    """Add and return a new student record."""
    # TODO: Add the validated student to the list and return it.
    pass


@app.get("/students/grade/{grade}")
def students_by_grade(grade: int):
    """Return students in one grade."""
    # TODO: Validate the grade and return matching students.
    pass
