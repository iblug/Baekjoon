import sys
from itertools import combinations_with_replacement as cwr
input = sys.stdin.readline

d = [i*(i+1)//2 for i in range(1, 47)]
c = list(cwr(d, 3))
m = int(input())
for _ in range(m): 
    n = int(input())
    for j in c:
        if sum(j) == n:
            print(1)
            break
    else:
        print(0)