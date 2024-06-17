n, a = map(int, input().split())
b = list(map(int, input().split()))

r = 0
for i in b:
    r += i//a
print(r)