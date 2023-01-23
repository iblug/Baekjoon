import sys
input = sys.stdin.readline
n = int(input())
data = []
for _ in range(n):
    age, name = input().split()
    age = int(age)
    data.append([age, name])
result = sorted(data, key=lambda x: x[0])
for r in result:
    print(*r)