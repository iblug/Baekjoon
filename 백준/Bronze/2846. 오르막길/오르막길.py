N = int(input())
p = list(map(int, input().split()))
step = 0
result = 0
for i in range(N-1):
    if (p[i]<p[i+1]):
        step += p[i+1]-p[i]
    else:
        step = 0
    result = max(result, step)
print(result)