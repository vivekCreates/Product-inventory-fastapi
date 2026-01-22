from pydantic import BaseModel


class Prodcut(BaseModel):
    id: int
    name:str
    price:int
    quantity:int
    
