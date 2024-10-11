import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if not n:
        break
    l = list(map(int, input().split()))
    r = 1e9
    a = 0
    for i in range(n):
        if r > abs(2023 - l[i]):
            r = abs(2023 - l[i])
            a = i + 1
    print(a)