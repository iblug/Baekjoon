n = int(input())
r = 0
for _ in range(n):
    a, b, c = map(int, input().split())
    if a == b == c:
        s = a*1000 + 10000
    elif a == b or a == c:
        s = a*100 + 1000
    elif b == c:
        s = b*100 + 1000
    else:
        s = max(a, b, c)*100
    
    if r < s:
        r = s
print(r)