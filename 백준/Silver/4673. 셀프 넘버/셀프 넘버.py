a = [i for i in range(1, 10000)]
for i in range(1, 10000):
    while(1):
        x = str(i)
        l = len(x)
        c = i
        for j in range(l):
            c += int(x[j])
        if c in a:
            a.remove(c)
        else:
            break
print(*a,sep='\n')