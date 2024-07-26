a = input()
b = input()

for (i, j) in zip(a, b):
    print(max(i, j), end='')