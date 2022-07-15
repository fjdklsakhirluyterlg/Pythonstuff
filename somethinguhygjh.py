import random


class Neural:
    def __init__(self, _size, _size1, _size2, _out):
        self.size = _size
        self.size1 = _size1
        self.size2 = _size2
        self.out = _out

    
    
    def layers(self, size, size1, size2, out):
        weights1 = []
        weights2 = []
        weights3 = []
        bias = []
        l = self.size*self.size1
        for index in range(0, l):
            weights1.append(random.randint(-6, 6))
        l1 = self.size1*self.size2
        for index in range(0, l1):
            weights2.append(random.randint(-6, 6))
        l2 = self.size2*self.out
        for index in range(0, l2):
            weights3.append(random.randint(0, l2))
        b = self.size + self.size1 + self.size2
        for index in range(0, b):
            bias.append(random.randint(-10, 10))
        
        z = 0
        for index in range(0, l):
          z + input[index]*weights1[index]
        

        
    

    
