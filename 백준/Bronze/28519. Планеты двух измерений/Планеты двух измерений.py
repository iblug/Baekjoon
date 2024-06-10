n, m = map(int, input().split())
if -1 <= n - m <= 1:
    print(n+m)
else:
    print(min(n, m)*2 + 1)
