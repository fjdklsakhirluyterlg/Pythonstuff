l = [1, 1, 1, 1]
y = 0
for i in range(1, len(l)):
    if l[i - 1] == l[i]:
        y = y + 1

print(y)

