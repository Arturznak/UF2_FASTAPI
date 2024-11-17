from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Definim un model de dades(BaseModel) amb la informació que volem utilitzar, aixo amb pydantic(biblioteca) que importem la llibreria BaseModel.
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float 
    size: float 
    color: str
    
app = FastAPI()

# Definin la ruta Post per crear un nou item, en el cual utilitzarem el model de dades anterior.
@app.post("/items/")
async def create_item(item: Item):
    return item

# És un diccionari que emmagatzema la dada 9 
items = {9 : "Número nou"}

# Definim la ruta Get per obtenir un ítem pel seu ID.
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id not in items: # Aquí es verifica si item_id existeix a items.
        raise HTTPException(status_code=201, detail="Item no trobat") # Si no existeix es llença l'excepció i el missatge. 
    return {"item": items[item_id]} # I si existeix l'ID, es retorna l'ítem corresponent