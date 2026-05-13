# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using Python and the FastAPI framework. You will define API routes, handle JSON data, and implement CRUD-style behavior for a small resources collection.

## 📝 Tasks

### 🛠️ Set up the FastAPI application

#### Description
Create a FastAPI app that includes the main application object and defines a root route.

#### Requirements
Completed program should:

- Use `FastAPI()` to create an application instance.
- Define a `GET /` route that returns a welcome message as JSON.
- Be runnable with `uvicorn`.

### 🛠️ Create resource endpoints

#### Description
Implement endpoints to manage a collection of books in memory using Python data structures.

#### Requirements
Completed program should:

- Define a `GET /books` route that returns the list of books.
- Define a `GET /books/{book_id}` route that returns a single book by ID.
- Define a `POST /books` route that accepts a new book and returns it with an assigned ID.
- Define a `PUT /books/{book_id}` route that updates an existing book.
- Define a `DELETE /books/{book_id}` route that removes a book.

### 🛠️ Validate and document the API

#### Description
Use FastAPI request and response validation features, and verify the API documentation.

#### Requirements
Completed program should:

- Use Pydantic models to validate incoming book data.
- Return JSON responses for all endpoints.
- Allow students to explore the automatic Swagger UI at `/docs`.
- Demonstrate the API using sample requests in comments or instructions.
