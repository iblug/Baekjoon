import sys
input = sys.stdin.readline

t = int(input())
s = set()
r = 0
for _ in range(t):
    a = input().rstrip()
    if a == "ENTER":
        r += len(s)
        s.clear()
    else:
        s.add(a)
r += len(s)
print(r)