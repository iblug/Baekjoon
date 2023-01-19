import sys

data = [a for a in map(int, sys.stdin.readlines()) if a % 2 == 1]
data.sort()
if data:
    print(sum(data))
    print(data[0])
else:
    print(-1)