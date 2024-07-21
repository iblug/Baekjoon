a = sorted([int(input()) for _ in range(3)])
if sum(a[:2]) == a[2]:
    print(1)
else:
    print(0)