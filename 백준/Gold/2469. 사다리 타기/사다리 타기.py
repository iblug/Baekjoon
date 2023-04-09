import sys
input = sys.stdin.readline

k = int(input().rstrip())
n = int(input().rstrip())
s = list(range(k))
e = [ord(x)-65 for x in list(input().rstrip())]
for m in range(n):
    lo = input().rstrip()
    if lo == '?'*(k-1):
        break
    for i in range(k-1):
        if lo[i] == '-':
            s[i], s[i+1] = s[i+1], s[i]
d = []
for _ in range(n-m-1):
    d.append(input().rstrip())
for lo in d[::-1]:
    for i in range(k-1):
        if lo[i] == '-':
            e[i], e[i+1] = e[i+1], e[i]
r = ''
for i in range(k-1):
    if s[i] == e[i]:
        r += '*'
    elif s[i] == e[i+1]:
        r += '-'
        s[i], s[i+1] = s[i+1], s[i]
    else:
        r = 'x'*(k-1)
        break
print(r)