import sys
input = sys.stdin.readline

n = int(input())
l = [0] * n
for i in range(n):
    a = int(input())
    l[a-1] = i + 1
print('\n'.join(map(str, l)))