import random

class Module(object):
    def __init__(self, integer, str):
        self.integer = integer
        self.str = str
    
    def generateRandom(self):
        random_number = random.randint(1, self.integer)

    def getText(self):
        print(f'Module {self.integer} printed: {self.str}')

    def zeroToInt(self):
        for i in range(self.integer):
            print(f'{self.integer} ')

