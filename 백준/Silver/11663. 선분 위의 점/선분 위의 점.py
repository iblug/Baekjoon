import sys
input = sys.stdin.readline

from bisect import bisect_left as bl
from bisect import bisect_right as br

n, m = map(int, input().split())
d = sorted(map(int, input().split()))

for _ in range(m):
    a, b = map(int, input().split())
    r = br(d, b) - bl(d, a)
    print(r)