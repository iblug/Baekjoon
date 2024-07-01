a = list(map(int, input().split()))
c = 0
for e in a[1:]:
    if a[0] - e <= 1000:
        c += 1
    else:
        break
print(c)