n = int(input())
l = list(map(int, input().split()))
p = list(map(int, input().split()))

s = 0
low = p[0]
for i in range(n-1):
    if p[i] <= low:
        low = p[i]
    s += low * l[i]
print(s)