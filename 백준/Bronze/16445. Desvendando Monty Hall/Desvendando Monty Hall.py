n = int(input())
l = [input() for _ in range(n)]
print(n - l.count('1'))
