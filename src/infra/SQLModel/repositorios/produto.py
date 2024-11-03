from sqlmodel import Session, select
from src.schemas import schemas
from src.infra.SQLModel.models import models


class RepositorioProduto():
    
    def __init__(self, db: Session):
        self.db = db
    
    def criar(self, produto: schemas.Produtos):
        db_produtos = models.Produto(nome = produto.nome, detalhes = produto.detalhes,
            preco = produto.preco, disponivel = produto.disponivel)
        
        self.db.add(db_produtos)
        self.db.commit()
        self.db.refresh(db_produtos)
        return db_produtos
    
    def listar(self):
        produtos = self.db.exec(select(models.Produto)).all()
        return produtos
    
    def obter(self):
        pass
    
    def remover(self):
        pass