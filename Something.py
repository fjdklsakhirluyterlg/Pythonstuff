z = int(integer("Enter a number: "))

def collatz(x):
    z = x
    n = [x]
    while x > 1:
        if x % 2 == 0:
            x = int(x / 2)
            n.append(x)
        else:
            x = int(3 * x + 1)
            n.append(x)
    else:
        print(f"The number {z} has a series of {n} and reached a peak of {max(n)} and was {len(n)} terms long")


for index in range(z):
    collatz(index)