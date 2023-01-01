a=[]
for _ in range(10):
    x = int(input())%42
    if x not in a:
        a.append(x)
print(len(a))