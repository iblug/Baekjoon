t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    r = 0
    for i in range(a, b+1):
        c = str(i)
        r += c.count('0')
    print(r)