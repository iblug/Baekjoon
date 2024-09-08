from itertools import combinations

l = list(map(int, input().split()))
p = [i | j for i, j in combinations(l, 2)]
t = [i | j | k for i, j, k in combinations(l, 3)]
r = 0
for i in p:
    r ^= i
for j in t:
    r ^= j
print(r)