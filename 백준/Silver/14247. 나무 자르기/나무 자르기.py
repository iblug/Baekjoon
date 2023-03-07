n = int(input())
h = list(map(int, input().split()))
a = list(map(int, input().split()))

cnt = sum(h)
a.sort()
for i in range(1, n):
    cnt += a[i]*i
print(cnt)