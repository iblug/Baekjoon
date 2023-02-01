n = int(input())
data = list(map(int, input().split()))
data = sorted(data)

cnt = 0
for i in range(1, n+1):
    cnt += data.pop()*i
print(cnt)