import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p, t = map(int, input().split())
    print(p + t//4 - t//7)