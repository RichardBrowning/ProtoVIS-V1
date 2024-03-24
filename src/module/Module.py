import random

class Module(object):
    def __init__(self, integer, str):
        self.integer = integer
        self.str = str
    
    def generateRandom(self):
        return random.randint(1, self.integer)

    def getText(self):
        return f'Module {self.integer} printed: {self.str}'

    def zeroToInt(self):
        for i in range(self.integer):
            print(f'{self.integer} ')

