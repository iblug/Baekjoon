import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    s = list(map(int, input().split()))
    s = sorted(s)
    print(s[-3])