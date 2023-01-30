a, b = input().split()
a = list(map(int, a.replace('0','')))
b = list(map(int, b.replace('0','')))
result = 0

for a1 in a:
    result += a1 * sum(b)
print(result)