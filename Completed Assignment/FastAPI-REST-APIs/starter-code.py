# Starter Code for Building REST APIs with FastAPI Assignment
# Run with: uvicorn starter-code:app --reload

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Task 1: Create Your First Endpoints


@app.get("/")
def read_root():
    # Return a welcome message
    return {"message": "Welcome to the FastAPI REST API!"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    # Return the Item at the given index in the items list
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


# Task 2: Use Request and Response Models


class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True


items: list[Item] = []


@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return item


@app.get("/items")
def list_items():
    return items


# Task 3: Handle Errors and Edge Cases


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    return items.pop(item_id)
