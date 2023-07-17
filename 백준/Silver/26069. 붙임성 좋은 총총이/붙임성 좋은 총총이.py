import sys
input = sys.stdin.readline

t = int(input())
s = {"ChongChong"}
for _ in range(t):
    a, b = input().split()
    if a in s:
        s.add(b)
    if b in s:
        s.add(a)
print(len(s))