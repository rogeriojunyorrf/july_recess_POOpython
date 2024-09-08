class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def preco(self):
        return self.__preco
    
    @nome.setter
    def nome(self, value):
        self.__nome = value
    
    @preco.setter
    def preco(self, value):
        self.__preco = value

    def __str__(self):
        return f'Nome: {self.__nome}, Preço: {self.__preco} '

