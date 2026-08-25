# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a REST API in Python using the FastAPI framework, including routes, request/response models, and basic error handling.

## 📝 Tasks

### 🛠️	Create Your First Endpoints

#### Description
Set up a FastAPI application with a few basic routes that return JSON data.

#### Requirements
Completed program should:

- Create a FastAPI app instance
- Define a `GET /` route that returns a welcome message
- Define a `GET /items/{item_id}` route that returns the item ID from the URL path
- Run the app locally using `uvicorn`

### 🛠️	Use Request and Response Models

#### Description
Define a Pydantic model to validate and structure the data your API accepts and returns.

#### Requirements
Completed program should:

- Define a Pydantic `Item` model with fields like `name`, `price`, and `in_stock`
- Add a `POST /items` route that accepts an `Item` in the request body and stores it in memory
- Add a `GET /items` route that returns the list of stored items

### 🛠️	Handle Errors and Edge Cases

#### Description
Add validation and error handling so the API responds correctly to invalid requests.

#### Requirements
Completed program should:

- Return a `404` error with a clear message when an item ID doesn't exist
- Return a `422` error automatically when request data fails validation
- Add a `DELETE /items/{item_id}` route that removes an item or returns a `404` if not found
