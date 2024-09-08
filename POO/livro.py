class Livro:
    def __init__(self, titulo, autor, disponivel = True):
        self.__titulo = titulo
        self.__autor = autor
        self.__disponivel = disponivel

    def emprestar(self):
        if self.__disponivel == True:
            self.__disponivel = False
            return f'O livro {self.__titulo} está disponível e será emprestado.'
        else:
            return f'O livro {self.__titulo} não está disponível.'
        
    def devolver(self):
        if self.__disponivel == False:
            self.__disponivel = True
            return f'O livro {self.__titulo} foi devolvido e está disponível novamente.'
        else:
            return f'O livro {self.__titulo} não foi emprestado.'
        
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def autor(self):
        return self.__autor
    
    @titulo.setter
    def titulo(self, value):
        self.__titulo = value
    
    @autor.setter
    def autor(self, value):
        self.__auto = value
        
    def __str__(self):
        return f'Título do livro: {self.__titulo}, Autor do livro: {self.__autor}'