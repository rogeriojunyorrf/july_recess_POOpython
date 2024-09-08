from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade


    pass #nome, idade (getters)
class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self._dados = []
    
    def criar_conta(self, agencia, conta, saldo):
        while True:
            tipo = int(input('Escolha uma conta: \n 1 - Conta Corrente \n 2 - Conta Poupança'))
            try:
                if tipo == 1:
                    self._dados.append(ContaCorrente(agencia, conta, saldo))
                    return f'{self._nome}, sua conta corrente foi criada! '
                elif tipo == 2:
                    self._dados.append(ContaPoupanca(agencia, conta, saldo))
                    return f'{self._nome}, sua conta poupança foi criada! '
            except ValueError:
                print('Erro! Input inválido')
    def sacar(self):
        Conta.sacar()

class Banco:
    pass
    #conta e agencias
    #tem que checar se a agencia, cliente e conta são daquele banco (todos os 3 pro saque ser permitido)
class Conta:
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia
    
    @property
    def conta(self):
        return self._conta
    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        if isinstance(valor, (int, float)):
            raise ValueError('Saldo precisa ser numérico.')
        self._saldo = valor
    
    def depositar(self, valor):
        if isinstance(valor, (int, float)):
            raise ValueError('Depósito precisa ser numérico.')
        self._saldo += valor
    
    def sacar(self, valor):
        pass 

    #método abstrato(?) sacar
    
class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite = 100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite


class ContaPoupanca(Conta):
    def __init__(self, agencia, conta, saldo):
        super().__init__()



c = Cliente('Sthe',16)
c.criar_conta('a','b',2122)
c.sacar()


# se eu não me engano, quando fui fazer isso meu recesso já estava no fim e eu precisava estudar outras matérias. 
# não deu pra finalizar 