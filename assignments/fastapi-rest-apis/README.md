# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API with FastAPI that lets users view, create, update, and delete book records. You will practice defining routes, using path parameters, validating request data, and returning appropriate HTTP responses.

## 📝 Tasks

### 🛠️ Set Up the FastAPI Application

#### Description

Use the provided starter code to create a FastAPI application and run it with Uvicorn. Confirm that the application is available locally and that FastAPI's interactive documentation page opens in your browser.

#### Requirements

Completed program should:

- Import `FastAPI` and create an application instance named `app`.
- Run locally with `uvicorn starter-code:app --reload`.
- Provide a `GET /` route that returns a JSON welcome message.
- Make the interactive API documentation available at `/docs`.

### 🛠️ Create Book API Endpoints

#### Description

Add endpoints that manage books stored in the starter code's in-memory list. Use a Pydantic model to validate data sent when a book is created or updated.

#### Requirements

Completed program should:

- Provide `GET /books` to return every book and `GET /books/{book_id}` to return one book by ID.
- Provide `POST /books` to add a book with a title and author validated by a Pydantic model.
- Provide `PUT /books/{book_id}` to update an existing book and `DELETE /books/{book_id}` to remove one.
- Return a `404 Not Found` response when a requested book ID does not exist.
- Test each endpoint from `/docs` and verify that successful requests return JSON responses.
