# https://www.acmicpc.net/problem/4673

a = [i for i in range(1, 10000)]
for i in range(1, 10000):
    while(1):
        c = i
        for _ in range(4):
            c += i%10
            i //= 10
        if c in a:
            a.remove(c)
        else:
            break
print(*a,sep='\n')