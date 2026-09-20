# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI that lets clients view and add student records. You will practice defining routes, accepting JSON request bodies with Pydantic models, validating input, and returning useful HTTP responses.

## 📝 Tasks

### 🛠️ Create a Read-Only Student Endpoint

#### Description

Complete the starter application so it can run with Uvicorn and expose a `GET /students` endpoint. The endpoint should return the in-memory student records as JSON.

To run the API locally, install FastAPI and Uvicorn, then start the server:

```bash
pip install fastapi uvicorn
uvicorn starter-code:app --reload
```

Visit `http://127.0.0.1:8000/docs` to use FastAPI's interactive documentation.

#### Requirements
Completed program should:

- Create a FastAPI application named `app`
- Implement `GET /students`
- Return the complete list of student records as JSON
- Return an empty list or a clear message when no records exist


### 🛠️ Add and Validate New Students

#### Description

Define a Pydantic model for a student and implement `POST /students`. The route should accept a JSON request body, validate the required fields, add the new student to the in-memory list, and return the created record.

Example request:

```json
{
  "name": "Avery Chen",
  "grade": 10,
  "favorite_subject": "Computer Science"
}
```

#### Requirements
Completed program should:

- Define a Pydantic model with required `name`, `grade`, and `favorite_subject` fields
- Reject invalid input such as a missing name or a grade outside the range 9 through 12
- Implement `POST /students`
- Return the newly created student with HTTP status `201`
- Keep the new student available from later `GET /students` requests


### 🛠️ Find Students by Grade

#### Description

Add a filtered endpoint, `GET /students/grade/{grade}`, that returns only students in the requested grade. Handle grades that are valid but have no matching students with an empty JSON list.

#### Requirements
Completed program should:

- Accept the grade as a path parameter
- Return only records whose grade matches the requested grade
- Return HTTP status `404` with a helpful detail message for an invalid grade
- Return an empty list when a valid grade has no matching students
