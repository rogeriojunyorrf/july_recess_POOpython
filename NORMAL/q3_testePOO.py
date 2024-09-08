class Questao3:
    def __init__(self):
        self.matriz = []
        self.populated = False
        self.l = 0
        self.c = 0
    
    def get_matriz(self):
        if not self.populated:
            return self.matriz
        for i in range(self.l):
            print(self.matriz[i])
    
    
    def populate(self):
        if self.populated:
            print('Already populated')
            return
        while True:
            try:
                l = int(input('Type i: (i > 1 / i = int): '))
                c = int(input('Type j: (j > 1 / j = int): '))
        # dava pra pedir só a ordem já que só dá pra fazer com matriz quadrada (não to com tempo pra alterar, tenho que dormir :( )
                if l > 1 and c > 1 and l == c:
                    break
            except ValueError:
                'Error'
        self.l = l
        self.c = c
        for i in range(l):
            line = []
            for j in range(c):
                line.append(int(input('Type a number: ')))
            self.matriz.append(line)
        self.populated = True

    def transform(self):
        if not self.populated:
            print('U need to populate first! ')
            return
        tmatriz = []
        for i in range(self.l):
            line = []
            for j in range(self.c):
                line.append(0)
            tmatriz.append(line)
        for i in range(self.l):
            for j in range(self.c):
                tmatriz[i][j] = self.matriz[j][i]
        for i in range(self.l):
            print(tmatriz[i])

q = Questao3()
q.populate()
print(q.get_matriz())
q.transform()

        
