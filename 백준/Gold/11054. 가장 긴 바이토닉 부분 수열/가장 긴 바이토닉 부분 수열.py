n = int(input())
d = list(map(int, input().split()))
dp_l = [1]*n
dp_r = [1]*n
for i in range(n):
    for j in range(i):
        if d[j] < d[i] :
            dp_l[i] = max(dp_l[j]+1, dp_l[i])
for i in reversed(range(n)):
    for j in range(n-1, i-1, -1):
        if d[j] < d[i] :
            dp_r[i] = max(dp_r[j]+1, dp_r[i])
dp = [dp_l[i]+dp_r[i] for i in range(n)]
print(max(dp)-1)