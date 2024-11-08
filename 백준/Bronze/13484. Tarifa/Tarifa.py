X = int(input())
N = int(input())

r = X*(N+1)
for _ in range(N):
    p = int(input())
    r -= p
print(r)