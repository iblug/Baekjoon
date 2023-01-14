# https://www.acmicpc.net/problem/2798
# 블랙잭

import sys
sys.stdin = open('input.txt', 'r')

from itertools import combinations

n, m = map(int, input().split())
s = list(map(int, input().split()))

r = 1e9

for i in list(combinations(s, 3)):
    if sum(i) == m:
        p = m
        break
    if m >= sum(i) and r != min(r, m - sum(i)):
        r = min(r, m - sum(i))
        p = sum(i)
print(p)

###
# combinations 안쓰고 그냥 풀자..