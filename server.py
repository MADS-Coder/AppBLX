from fastapi import FastAPI, Depends
from sqlmodel import Session
from src.schemas.schemas import Produtos
from src.infra.SQLModel.config.database import get_session, create_db_and_tables
from src.infra.SQLModel.repositorios.produto import RepositorioProduto

create_db_and_tables()

app = FastAPI()

@app.post('/produtos')
def criar_produtos(produto: Produtos, db: Session = Depends(get_session)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@app.get('/produtos')
def lista_produtos(db: Session = Depends(get_session)):
    lista_produtos = RepositorioProduto(db).listar()
    return lista_produtos