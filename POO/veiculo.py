class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def descricao(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano} '

    
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, num_portas):
        super().__init__(marca, modelo, ano)   
        self.num_portas = num_portas

    def descricao(self):
        return super().descricao() + f'Número de Portas: {self.num_portas}'


class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, tipo_de_motor):
        super().__init__(marca, modelo, ano)
        self.tipo_de_motor = tipo_de_motor

    def descricao(self):
        return super().descricao() + f'Tipo de Motor: {self.tipo_de_motor} '
    