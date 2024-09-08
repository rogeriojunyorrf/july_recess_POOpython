class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def desconto(self, percent):
        self.price = self.price - self.price * (percent / 100)       
        
    @property
    def price(self):
        self.price = self._price
        return self._price
    #classes.py
    
    @price.setter
    def price(self, value):
        self._price = float(value.replace('R$',''))


