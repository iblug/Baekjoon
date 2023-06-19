import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    r = []
    a, b  = input().split()
    for i in range(len(a)):
        if (c:=ord(a[i])) > (d:=ord(b[i])):
            r.append(d-c+26)
        else:
            r.append(d-c)
    print('Distances:', ' '.join(map(str, r)))