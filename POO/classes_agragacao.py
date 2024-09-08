class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []
    
    def inserir_produto(self, produto):
        self.produtos.append(produto)
    
    def lista_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total
    # essa classe pode exisitir sozinha, mas é dependente de Produto

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    # essa classe pode existir sozinha e é independente
    