import sys
input = sys.stdin.readline

K = int(input())
for _ in range(K):
    P, M = map(int, input().split())
    s = {input().rstrip() for _ in range(P)}

    print(P-len(s))