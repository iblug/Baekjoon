import sys
input = sys.stdin.readline


d = [(int(input()), i) for i in range(1, 9)]
d = sorted(d)
r = 0
a = []
for e in d[-5:]:
    r += e[0]
    a.append(e[1])
print(r)
print(' '.join(map(str, sorted(a))))