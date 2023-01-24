n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
d = {}
for c in a:
    d[c] = d.get(c,0) +1
for e in b:
    print(d.get(e,0), end=' ')