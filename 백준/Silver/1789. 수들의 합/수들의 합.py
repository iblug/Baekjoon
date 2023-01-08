n = int(input())

cnt = 0

for i in range(1,(n+1)//2+1):
    if i + 1 > n - i:
        cnt += 1
        break
    n -= i
    cnt += 1
print(cnt)