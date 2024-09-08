class User:
    userCount = 0    
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        User.userCount += 1
    
    @classmethod
    def get_userCount(cls):
        return cls.userCount
    
    @classmethod
    def get_string(cls, fullname):
        firstName, lastName = fullname.split()
        return cls(firstName, lastName)
    
    def __str__(self):
        return f'{self.firstName} {self.lastName}'

#já o @staticmethod não pode receber self, nem cls, apenas variáveis locais e () vazio