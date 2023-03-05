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
            c1 = max(c1, l[i+2]-l[i])
        else:
            c2 = max(c2, l[i+2]-l[i])
    print(max(c1, c2))