from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float 
    size: float 
    color: str
    
app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.get("/items/{item_id}", status_code=201)
async def read_item(item_id: int):
    return {"item_id": item_id }