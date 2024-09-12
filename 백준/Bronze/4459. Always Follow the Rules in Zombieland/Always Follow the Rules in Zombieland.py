import sys
input = sys.stdin.readline

l = [0]
q = int(input())
for i in range(1, q+1):
    l.append(input().rstrip())
r = int(input())
for _ in range(r):
    a = int(input())
    if 0 < a <= q:
        print(f'Rule {a}: {l[a]}')
    else:
        print(f'Rule {a}: No such rule')