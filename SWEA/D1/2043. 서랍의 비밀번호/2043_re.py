# 제출한 답

p, k = list(map(int, input().split()))

cnt = 1
while k != p:
    k += 1
    cnt += 1
print(cnt) 


# 완전 쉽게

p, k = map(int, input().split())
print(p-k+1)