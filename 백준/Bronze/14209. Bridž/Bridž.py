import sys
input = sys.stdin.readline

l = {
    'A': 4,
    'K': 3,
    'Q': 2,
    'J': 1
}

n = int(input())
r = 0
for _ in range(n):
    s = input()
    for e in s:
        r += l.get(e, 0)
print(r)