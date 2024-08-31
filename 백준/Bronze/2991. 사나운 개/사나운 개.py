a, b, c, d = map(int, input().split())
e = list(map(int, input().split()))

for i in e:
    t = 0
    if 0 < i % (a + b) <= a:
        t += 1
    if 0 < i % (c + d) <= c:
        t += 1
        
    print(t)