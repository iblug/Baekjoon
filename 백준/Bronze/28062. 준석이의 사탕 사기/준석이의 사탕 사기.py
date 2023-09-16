n = int(input())
c = list(map(int, input().split()))
s = 0
m = 1001
for i in c:
    if i%2 and i < m:
        m = i
    s += i
if s % 2:
    print(s-m)
else:
    print(s)