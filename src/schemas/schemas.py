from pydantic import BaseModel
from typing import Optional


class Usuarios(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str


class Produtos(BaseModel):
    id: Optional[str] = None
    nome: str 
    detalhes: str
    preco: float
    disponivel: bool = False
    


class Pedidos(BaseModel):
    id: Optional[str] = None
    #usuario: Usuarios
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: str | None = None
