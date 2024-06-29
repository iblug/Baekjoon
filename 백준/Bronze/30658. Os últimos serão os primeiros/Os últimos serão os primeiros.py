import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    l = reversed([int(input()) for _ in range(n)])
    for e in l:
        print(e)
    print(0)
