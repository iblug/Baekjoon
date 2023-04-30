h, w = map(int, input().split())
d = list(map(int, input().split()))

s = []
total = 0
for i in range(w):
    while s and d[i] > d[s[-1]]:
        a = s.pop()
        if not s:
            break
        t = min(d[i], d[s[-1]]) - d[a]
        total += ((i-s[-1]-1) * t)
    s.append(i)
print(total)