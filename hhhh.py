import random

def generateπfrom_random(n):
    ins = 0
    total = 0
    for i in range(n):
        x = random.randint(0, 1)
        y = random.randint(0, 1)
        distance = x**2 + y**2
        if distance <= 1:
            ins += 1
        total +=1
    
    return 4*ins/total


print(generateπfrom_random(8000))