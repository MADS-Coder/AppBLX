# **App BLX - Aplicação BackEnd**

App para anúncio e vendas de produtos na vizinhança (no seu bairro ou povoado).

## **Funcionalidades**
Qualquer pessora poderá anunciar produtos
Qualquer pessoa poderá fazer pedidos dos produtos anunciados
Uma pessoa tem:
    nome
    telefone (whatsapp)
Um produto tem:
    nome
    detalhamento
    preço
    disponivel (sim/não)
    fotos(?)
Um pedido tem:
    Produto
    Pessoa que está pedindo
    Quantidade
    Local de entrega
    Entrega ou Retirada
    Observações (sabor, horario de entrega, troco, etc.)
Cada usuário terá uma lista de pedidos recebidos (minhas vendas) e pedidos feitos (minhas compras).
O pedido deverá ser aceito pelo vendedor
O comprador poderá acompanhar seus pedidos:
    Status (Feito, Aceito, A caminho)

## **Arquiteturas e Ferramenta**
Python + FastAPI (pydantic)
Será uma API Rest
Banco de Dados: Postgres e/ou MongoDB (firebase firestore)
Docker para Postgres
MVC
Domain Driven Design e Arquitetura Limpa (Clean Arch.)
