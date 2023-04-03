n = int(input())
v = list(map(int, input().split()))

if v.count(0) >= (n+1)//2:
    print('INVALID')
    exit()
if sum(v) > 0:
    print('APPROVED')
else:
    print('REJECTED')
