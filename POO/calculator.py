class Calculator:
    def __init__(self):
        self.vector = []
    
    def populate(self):
        while True:
            value = input('Type a value (type "exit" to stop): ')
            if value.lower() == "exit":
                break
            try:
                self.vector.append(float(value))
            except ValueError:
                print("Invalid input. Please enter a number.")
        return self.vector

    def add(self):
        result = sum(self.vector)
        print(f'The result(+) is {result}')
        return result
    
    def sub(self):
        if not self.vector:
            print('The vector is empty.')
            return
        result = self.vector[0]
        for value in self.vector[1:]:
            result -= value 
        print(f'The result(-) is {result}')
        return result
    
    def mult(self):
        if not self.vector:
            print('The vector is empty.')
            return
        result = self.vector[0]
        for value in self.vector[1:]:
            result *= value
        print(f'The result is {result}')
        return result
    
    def div(self):
        if not self.vector: 
            print('The vector is empty.')
            return
        result = self.vector[0]
        for value in self.vector[1:]:
            result /= value
        print(f'The result(/) is {result}')
        return result
    
