# https://www.acmicpc.net/problem/1789
# 수들의 합 - python 배우기

n = int(input())

cnt = 0

for i in range(1,(n+1)//2+1):
    if i + 1 > n - i:
        cnt += 1
        break
    n -= i
    cnt += 1
print(cnt)

# 속도 향상하기
# 다른 접근

# 같은 방식 다른사람의 코드

N = int(input())

i=1
sol=0
isSolve = False

while True:
    if N<i:
        isSolve = True
        break 
    if isSolve: break    
    N-=i
    i+=1
    sol+=1
    

print(sol)

################################################

# 원하는 답인것 같다
# 1부터 더하다가(cnt += 1) n보다 큰값이 나오면 그 직전의 cnt가 답

n=int(input())
sum=0
result=0
for i in range(1, n+1):
  sum+=i
  result+=1
  if sum>n:
    result-=1
    break
    
print(result)

###

s = int(input())
n = 1
while n * (n + 1) / 2 <= s:
    n += 1
print(n - 1)

#####################################################
# 원리가 뭘까
# 이진 탐색?

S = int(input())

start = 1
end = S
ans = 0
while start <= end:
    mid = (start + end) // 2
    if (mid * (mid + 1))//2 <= S:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1
        
print(ans)

#######################################################


# 숏코딩

print(int(((1+int(input())*8)**.5-1)/2))

###

print(int((2*int(input())+1/4)**(1/2)-1/2))