"""Starter FastAPI app for the 'Building REST APIs with FastAPI' assignment.

Run with:
    uvicorn starter-code:app --reload --port 8000

This file intentionally keeps state in-memory for simplicity.
"""
from typing import Optional, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI REST API - Starter")


class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float


# simple in-memory "database"
_items: List[Item] = [Item(id=1, name="Sample", description="A sample item", price=9.99)]


@app.get("/", tags=["root"])
async def read_root():
    return {"message": "Welcome to the FastAPI starter app. See /docs for API docs."}


@app.get("/items", response_model=List[Item], tags=["items"])
async def list_items():
    return _items


@app.get("/items/{item_id}", response_model=Item, tags=["items"])
async def get_item(item_id: int):
    for item in _items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items", response_model=Item, tags=["items"])
async def create_item(item: Item):
    # assign a simple incremental id if not provided
    next_id = max((i.id for i in _items), default=0) + 1
    item.id = next_id
    _items.append(item)
    return item
