import sys
input = sys.stdin.readline

def f(s, e, a, i):
    while s <= e:
        mid = (s+e)//2
        if i > a[mid]:
            s = mid + 1
        elif i < a[mid]:
            e = mid -1
        else:
            return 1
    return 0

T = int(input())
for _ in range(T):
    n = int(input())
    a = sorted(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    for i in b:
        print(f(0, n-1, a, i))