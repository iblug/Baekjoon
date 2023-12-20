import sys
input = sys.stdin.readline

a = [int(input()) for _ in range(6)]
b = sorted(a[:4]) 

print(sum(b[1:]) + max(a[4:]))
