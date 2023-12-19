import sys
input = sys.stdin.readline

n, m = map(int, input().split())

for _ in range(n):
    s = input().rsplit()
    for i in reversed(range(m)):
        print(s[0][i], end='')
    print()