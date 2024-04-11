import sys
input = sys.stdin.readline

di = ['N', 'E', 'S', 'W']
d = 0
for _ in range(10):
    d += int(input())

print(di[d%4])