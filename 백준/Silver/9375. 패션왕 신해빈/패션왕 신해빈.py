import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    data = {}
    n = int(input())
    for _ in range(n):
        _, b = input().split()
        data[b] = data.get(b,1) + 1
    result = 1
    for i in data.values():
        result *= i
    print(result-1)