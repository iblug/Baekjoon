n = int(input())

d = list(map(int, input().split()))
s = []
a = []
for i in range(n):
    while s:
        if d[i] < s[-1][1]:
            print(s[-1][0]+1, end=' ')
            break
        s.pop()
    if not s:
        print(0, end=' ')
    s.append((i, d[i]))