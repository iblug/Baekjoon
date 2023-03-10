from itertools import permutations

n, k = map(int, input().split())
a = list(map(lambda x:int(x)-k, input().split()))
a = permutations(a,n)
c = 0
for e in a:
    s = 0
    for i in e:
        s += i
        if s < 0:
            break
    else:
        c += 1

print(c)