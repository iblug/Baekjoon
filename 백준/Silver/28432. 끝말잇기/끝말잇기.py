import sys
input = sys.stdin.readline

n = int(input())
d = []
s = ''
e = ''
for i in range(n):
    a = input().rstrip()
    if a == '?':
        b = i
    d.append(a)
m = int(input())
if b == 0:
    if n == 1:
        print(input().rstrip())
    else:
        e = d[1][0]
        for i in range(m):
            a = input().rstrip()
            if a[-1] == e and a not in d:
                print(a)
                break
elif b == n-1:
    s = d[b-1][-1]
    for i in range(m):
        a = input().rstrip()
        if a[0] == s and a not in d:
            print(a)
            break
else:
    s = d[b-1][-1]
    e = d[b+1][0]
    for i in range(m):
        a = input().rstrip()
        if a[0] == s and a[-1] == e and a not in d:
            print(a)
            break
