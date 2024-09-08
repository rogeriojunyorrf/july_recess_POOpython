class Person:

    current_year = 2024

    def __init__(self, name, age, eating = False, talking = False):
        self.name = name
        self.age = age
        self.eating = eating
        self.talking = talking
    
    def eat(self, food):
        if self.eating:
            print(f'{self.name} already ate!')
            return
        if self.talking:
            print('stop talking first')
        print(f'{self.name} is eating {food}!')
        self.eating = True
    
    def stop_eating(self):
        if not self.eating:
            print('Bro is not eating')
            return
        print(f'{self.name} stoped eating!')
        self.eating = False
    
    def talk(self, friend):
        if self.talking:
            print('oh, bih is talking af')
            return
        if self.eating:
            print("paia af talk while eat")
            return
        print(f'{self.name} is talking with his/her friend {friend}')
        self.talking = True
    
    def stop_talking(self):
        if not self.talking:
            print(f'{self.name}s not talking right now')
            return
        print('finally stopped talking, amen')
        
    def born_year(self):
        print(f'The year {self.name} was born was {self.current_year - self.age}')
    
    def __str__(self):
        return f'{self.name} {self.age}' 