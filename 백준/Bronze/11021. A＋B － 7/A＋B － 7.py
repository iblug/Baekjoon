import sys
input = sys.stdin.readline
t = int(input())
for i in range(1, t + 1):
    print('Case #',i,': ',sum(map(int, input().split())),sep='')
