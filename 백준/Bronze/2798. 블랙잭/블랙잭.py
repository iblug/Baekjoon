n, m = map(int, input().split())
c = list(map(int, input().split()))

max_value = 9
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            now = c[i] + c[j] + c[k]
            if now <= m:
                max_value = max(now, max_value)
print(max_value)