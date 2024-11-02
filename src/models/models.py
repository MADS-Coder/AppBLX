from pydantic import BaseModel
from typing import Optional, List


class Usuarios(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
    meus_produtos: List[Produtos] # type: ignore
    minhas_vendas: List[Pedidos] # type: ignore
    meus_pedidos: List[Pedidos] # type: ignore


class Produtos(BaseModel):
    id: Optional[str] = None
    usuario: Usuarios
    nome: str 
    detalhes: str
    preco: float
    disponivel: bool = False


class Pedidos(BaseModel):
    id: Optional[str] = None
    usuario: Usuarios
    produto: Produtos
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = "Sem observações"