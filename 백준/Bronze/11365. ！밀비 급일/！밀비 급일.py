import sys
input = sys.stdin.readline

while 1:
    d = input().rstrip()
    if d == 'END':
        break
    print(d[::-1])
