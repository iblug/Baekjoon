import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s = input().rstrip()
    if s == '':
        break
    print(s.lower())