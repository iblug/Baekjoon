y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

a = y2 - y1
if (m2, d2) < (m1, d1):
    a -= 1
print(a)
print(y2-y1+1)
print(y2-y1)