import sys
input = sys.stdin.readline

def re(k):
    global result, ans

    if len(result) >= l-1 and n >= int(result):
        ans = max(ans, int(result))

    if len(result) == l:
        return

    for i in range(m):
        result += k[i]
        re(k)
        result = result[:-1]

n, m = input().split()
l = len(n)
n = int(n)
m = int(m)

k = list(input().split())
result = ''
ans = 0
re(k)
print(ans)