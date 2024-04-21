import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s = input().rstrip()
    print(s)
    c, p = map(int, s.split())
    print(c*p - (c-1)*2)
