import sys
input = sys.stdin.readline

def fibo(x):
    if d[x]:
        return d[x]
    else:
        d[x] = fibo(x-5) + fibo(x-1)
        return d[x]

t = int(input())
d = [0, 1, 1, 1, 2, 2] + [0]*95
for _ in range(t):
    a = int(input())
    print(fibo(a))