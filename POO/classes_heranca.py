class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__
    
    def falar(self):
        print(f'{self.nomeclasse} falando...')


class Cliente(Pessoa):
    def comprar(self):
        print('Comprando...')

# class Aluno(Pessoa):
#     def estudar(self):
#         print('Estudando...')


class ClienteVIP(Cliente):
    def __init__(self, nome, idade):
        super().__init__ # Pessoa.__init__ tbm funciona
    def falar(self):
        Pessoa.falar()
        super().falar()
        print('sou vip!')

