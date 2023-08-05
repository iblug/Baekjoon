import sys
input = sys.stdin.readline
n = int(input())
d = [int(input()) for _ in range(n)]
dp = [d[0]]
if n > 1:
    dp.append(d[0]+d[1])
if n > 2:
    dp.append(max(d[2]+d[1], d[2]+d[0], dp[1]))
    for i in range(3, n):
        dp.append(max(dp[i-2]+d[i], dp[i-3]+d[i-1]+d[i], dp[i-1]))
print(dp[n-1])