a, b = input().split()
result = 0
sum_ = sum(map(int, b))
for a1 in a:
    result += int(a1) * sum_
print(result)