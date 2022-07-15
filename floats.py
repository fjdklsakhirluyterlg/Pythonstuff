li = [9, 9, 7, 5, 3, 10, 2]

if all(li) >= 0:
    print(True)


def gen(x: int):
    for i in range(x):
        yield i**2

z = gen(8)
for i in z:
    print(next(z))

