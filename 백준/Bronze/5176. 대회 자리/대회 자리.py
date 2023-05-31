import sys
input = sys.stdin.readline

K = int(input())
for _ in range(K):
    P, M = map(int, input().split())
    s = set()
    cnt = 0
    for _ in range(P):
        a = int(input())
        if a in s:
            cnt += 1
        else:
            s.add(a)
    print(cnt)