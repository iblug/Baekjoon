# 처음 제출한 답
a=[]
m=0
for i in range(9):
    a.append(int(input()))
    if a[i] > m:
        m = a[i]
        c = i+1
print(m, c, sep="\n")

# 개선한 답
m=0
for i in range(9):
    a = int(input())
    if a > m:
        m = a
        c = i+1
print(m, c, sep="\n")
# 리스트 필요없다 바로바로 처리


##### 리스트 컴플리헨션
a = [int(input()) for _ in range(9)]
print(max(a))
print(a.index(max(a))+1)