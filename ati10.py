#Crie duas classes: Produto (nome, preço) e Carrinho 
# (que armazena produtos e suas quantidades). Implemente métodos no carrinho 
# para adicionar itens, remover itens, aplicar um cupom de desconto percentual 
# e calcular o valor total da compra.
class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

class Carrinho:
    def __init__(self):
        # Dicionário no formato: {nome_produto: {"produto": obj_produto, "quantidade": int}}
        self.itens = {}
        self.desconto_percentual = 0.0

    def adicionar_item(self, produto: Produto, quantidade: int = 1):
        if produto.nome in self.itens:
            self.itens[produto.nome]["quantidade"] += quantidade
        else:
            self.itens[produto.nome] = {"produto": produto, "quantidade": quantidade}

    def remover_item(self, nome_produto: str):
        if nome_produto in self.itens:
            del self.itens[nome_produto]

    def aplicar_cupom(self, percentual: float):
        if 0 <= percentual <= 100:
            self.desconto_percentual = percentual

    def calcular_total(self) -> float:
        subtotal = sum(
            item["produto"].preco * item["quantidade"]
            for item in self.itens.values()
        )
        desconto = subtotal * (self.desconto_percentual / 100)
        return subtotal - desconto
p1 = Produto("Teclado Mecânico", 250.00)
p2 = Produto("Mouse Sem Fio", 120.00)

carrinho = Carrinho()
carrinho.adicionar_item(p1, 1)
carrinho.adicionar_item(p2, 2)
carrinho.aplicar_cupom(10)
print(f"Total da compra com desconto: R$ {carrinho.calcular_total():.2f}")
