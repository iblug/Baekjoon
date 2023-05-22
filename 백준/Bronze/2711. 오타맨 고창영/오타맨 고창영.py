import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = input().split()
    a = int(a)-1
    print(b[:a], b[a+1:], sep='')