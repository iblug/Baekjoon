# https://www.acmicpc.net/problem/11050
# 이항 계수 1
N, K = map(int, input().split())

a = 1
b = 1
for i in range(N-K+1, N+1):
    a *= i
for j in range(1, K+1):
    b *= j
print(a//b)

# 공식 기억하기
# 다른 풀이 보기
# math 라이브러리