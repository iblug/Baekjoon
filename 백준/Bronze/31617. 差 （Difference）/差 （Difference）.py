k = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

r = 0
for e in b:
    r += a.count(e-k)
print(r)