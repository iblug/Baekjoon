from itertools import combinations

data = [int(input()) for _ in range(9)]
coms = combinations(data, 7)

for com in coms:
    if sum(com) == 100:
        print(*sorted(com), sep='\n')
        break