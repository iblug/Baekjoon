import sys
input = sys.stdin.readline

while 1:
    n = int(input())
    if n == 0:
        break
    print((n+1)*n//2)