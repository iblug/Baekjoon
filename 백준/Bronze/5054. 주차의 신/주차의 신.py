import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    x = list(map(int, input().split()))
    r = (max(x)-min(x))*2
    print(r)