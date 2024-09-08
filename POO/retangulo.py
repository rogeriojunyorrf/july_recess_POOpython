class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura
    
    def calcular_area(self):
        area = self.altura * self.largura
        print(f'A área é de: {area} cm')
    
    def calcular_perimetro(self):
        perimetro = (self.altura * 2) + (self.largura * 2)
        print(f'A perímetro é de: {perimetro}')