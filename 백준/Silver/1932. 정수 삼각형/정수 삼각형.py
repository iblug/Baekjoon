import sys
input = sys.stdin.readline

n = int(input())
dp = [([0]+list(map(int, input().split()))+[0]) for _ in range(n)]
for i in range(1, n):
    for j in range(1, i+2):
        dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
print(max(dp[-1]))