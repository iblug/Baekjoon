import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    L = list(map(int, input().split()))
    l = sorted(L)
    c1 = c2 = 0
    for i in range(n-2):
        if i & 1:
            c11 = l[i+2]-l[i]
            if c11 > c1:
                c1 = c11
        else:
            c22 = l[i+2]-l[i]
            if c22 > c2:
                c2 = c22
    print(max(c1, c2))