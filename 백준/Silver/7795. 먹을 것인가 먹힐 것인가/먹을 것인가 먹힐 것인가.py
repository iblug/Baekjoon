import sys
input = sys.stdin.readline

def bs(lo, hi):
    if lo+1 >= hi:
        return hi
    mid = lo+hi >> 1
    if B[mid] < i:
        return bs(mid, hi)
    else:
        return bs(lo, mid)


T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = sorted(map(int, input().split()))
    c = 0
    for i in A:
        c += bs(-1, m)
    print(c)