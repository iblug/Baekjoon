import sys
input = sys.stdin.readline

n, m = map(int, input().split())
c = 0
o = [input().rstrip() for _ in range(n)]
input()
for e in o:
    s = input().rstrip()
    for i in range(m):
        if s[i] == e[i]:
            c += 1
print(c)