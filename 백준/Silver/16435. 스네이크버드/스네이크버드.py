n, l = map(int, input().split())
h = sorted(map(int, input().split()))
for i in h:
    if l >= i:
        l += 1
print(l)