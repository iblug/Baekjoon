from itertools import combinations

d = [int(input()) for _ in range(9)]
s = combinations(d, 7)

for c in s:
    if sum(c) == 100:
        print(*sorted(c), sep='\n')
        break