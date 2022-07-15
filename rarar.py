def hi(*x):
    return [i**2 for i in x]

li = [3, 2, 4, 6, 7, 8, 1, 9]
print(hi(li))