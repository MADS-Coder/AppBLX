from sqlmodel import SQLModel, Field
from typing import Optional

class Produto(SQLModel, table = True):
    
    __tablename__='produto'
    
    id:  Optional[int] = Field(default=None, primary_key=True)
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False

