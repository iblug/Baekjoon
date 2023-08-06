n = int(input())
d = list(map(int, input().split()))
dp = [0]*n

for k in range(n):
    dp[k] = 1
    for i in range(k):
        if d[i] < d[k]:
            dp[k] = max(dp[k], dp[i] + 1)
print(max(dp))