import sys
input = sys.stdin.readline

n = int(input())
d = [int(input()) for _ in range(n)]
dp = [0]*n

dp[0] = d[0]
if n > 1:
    dp[1] = d[0]+d[1]
if n > 2:
    dp[2] = max(d[2]+d[1], d[2]+d[0], dp[1])
for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-3]+d[i-1]+d[i], dp[i-2]+d[i])
print(dp[n-1])