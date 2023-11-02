l, p = map(int, input().split())
a = list(map(int, input().split()))
for i in range(5):
    a[i] -= l * p
print(' '.join(map(str, a)))