# Starter Code for Building REST APIs with FastAPI Assignment
# Run with: uvicorn starter-code:app --reload

from fastapi import FastAPI

app = FastAPI()

# Task 1: Create Your First Endpoints
# Fill in the routes below

@app.get("/")
def read_root():
    # Return a welcome message
    pass

@app.get("/items/{item_id}")
def read_item(item_id: int):
    # Return the item ID from the path
    pass

# Task 2: Use Request and Response Models
# Define an Item model and in-memory storage

# from pydantic import BaseModel
#
# class Item(BaseModel):
#     name: str
#     price: float
#     in_stock: bool = True
#
# items = []
#
# @app.post("/items")
# def create_item(item: Item):
#     pass
#
# @app.get("/items")
# def list_items():
#     pass

# Task 3: Handle Errors and Edge Cases
# Add proper error handling for missing items

# @app.delete("/items/{item_id}")
# def delete_item(item_id: int):
#     pass
