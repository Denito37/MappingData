from pydantic import BaseModel

class Fountain(BaseModel):
    id: str
    updated_at:str
    located_at:str
    borough:str
    department:str
    status:str
    coordinates:str

class Tree(BaseModel):
    id:str
    updated_at:str
    name:str
    borough:str
    district:str
    status:str
    coordinates:str