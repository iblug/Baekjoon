data = set(int(input()) for _ in range(9))

over = sum(data) - 100
for i in data:
    if (over - i) in data:
        result = sorted(data-{i, over-i})
        break
print(*result, sep='\n')