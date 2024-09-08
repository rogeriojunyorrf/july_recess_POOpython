from datetime import datetime

class Pessoa:
    ano = datetime.now().strftime('%Y')
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 
    

class Dev(Pessoa):
    def __init__(self, nome, idade, amada, linguagem, nivel):
        super().__init__(nome, idade)
        self._amada = amada
        self.linguagem = linguagem
        self.nivel = nivel

    @property 
    def amada(self):
        return f'{self._amada} <3'
    
    @property
    def linguagem(self):
        return self._linguagem
    
    @linguagem.setter
    def linguagem(self, nova_linguagem):
        self._linguagem = nova_linguagem
    
    

    def __str__(self):
        return f'Nome: {self.nome}\nIdade: {self.idade}\nAmada: {self._amada}\nLinguagem: {self.linguagem}\nNível: {self.nivel}'
    

dev = Dev('Rogério', 16, 'Sthe', 'Python', 'Sênior')
print(dev)
print(dev.amada)