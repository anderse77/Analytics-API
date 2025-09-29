from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()
_DB = [{"id": 1, "name": "widget", "score": 42}]

class Item(BaseModel):
    id: int
    name: str
    score: int

@router.get("/", response_model=List[Item])
def list_items():
    return _DB

@router.post("/", response_model=Item, status_code=201)
def add_item(item: Item):
    if any(x["id"] == item.id for x in _DB):
        raise HTTPException(409, "id exists")
    _DB.append(item.model_dump())
    return item