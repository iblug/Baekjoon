x = {i for i in range(1, 31)}
a = []
for _ in range(28):
    a.append(int(input()))
x = x - set(a)
x = list(x)
x.sort()
print(*x,sep='\n')