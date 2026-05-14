# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using FastAPI. You will learn how to create endpoints that handle HTTP requests, work with request/response data, and structure an API following REST principles.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Application

#### Description
Set up a FastAPI application with a simple endpoint that returns data in JSON format.

#### Requirements
Completed program should:

- Import FastAPI and create an app instance.
- Create a GET endpoint at `/` that returns a welcome message as JSON (e.g., `{"message": "Welcome to the API"}`).
- Create a GET endpoint at `/items` that returns a list of sample items (e.g., a list of dictionaries with item names and prices).
- Test the API by running it with `uvicorn` and verifying the endpoints return expected responses.


### 🛠️ Add Path Parameters and Query Parameters

#### Description
Extend the API to accept user input through URL paths and query strings.

#### Requirements
Completed program should:

- Create a GET endpoint at `/items/{item_id}` that accepts an item ID from the path and returns details for that item.
- Create a GET endpoint at `/search` that accepts a `q` query parameter and returns matching items based on the search term.
- Both endpoints should return appropriate JSON responses with the requested data.


### 🛠️ Handle POST Requests

#### Description
Implement an endpoint that accepts data from the client and processes it.

#### Requirements
Completed program should:

- Create a POST endpoint at `/items` that accepts a JSON request body with item details (name and price).
- Validate that the request contains required fields.
- Return a JSON response confirming the item was received (e.g., `{"status": "Item added", "item": {...}}`).


### 🛠️ Add Error Handling and Status Codes

#### Description
Implement proper HTTP status codes and error responses.

#### Requirements
Completed program should:

- Return `404 Not Found` when an item ID doesn't exist in `/items/{item_id}`.
- Return `400 Bad Request` when required fields are missing in POST requests.
- Return `200 OK` for successful requests and `201 Created` for successful item creation.
- Include descriptive error messages in JSON responses.
