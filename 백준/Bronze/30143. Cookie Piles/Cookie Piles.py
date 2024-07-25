import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n, a, d = map(int, input().split())
    print(n*(2*a+(n-1)*d)//2)