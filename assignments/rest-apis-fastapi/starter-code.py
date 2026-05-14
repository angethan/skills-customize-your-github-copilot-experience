from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Sample data
items_db = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Mouse", "price": 29.99},
    {"id": 3, "name": "Keyboard", "price": 79.99},
]


# Pydantic model for request body validation
class Item(BaseModel):
    name: str
    price: float


# Task 1: Create basic endpoints
@app.get("/")
def read_root():
    # Return a welcome message
    pass


@app.get("/items")
def get_all_items():
    # Return all items from items_db
    pass


# Task 2: Add path and query parameters
@app.get("/items/{item_id}")
def get_item(item_id: int):
    # Find and return the item with the given ID
    # Return 404 if not found
    pass


@app.get("/search")
def search_items(q: str):
    # Search for items by name (case-insensitive)
    # Return matching items
    pass


# Task 3: Handle POST requests
@app.post("/items")
def create_item(item: Item):
    # Add a new item to items_db
    # Return the created item with a new ID
    pass


# Note: For running this API, use the command:
# uvicorn starter-code:app --reload
