x = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}
a = []
for _ in range(28):
    a.append(int(input()))
x = x - set(a)
x = list(x)
x.sort()
print(*x,sep='\n')