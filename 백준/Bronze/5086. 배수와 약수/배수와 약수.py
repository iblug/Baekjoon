import sys
input = sys.stdin.readline

while 1:
    a, b = map(int, input().split())
    if a or b:
        if not a % b:
            print('multiple')
        elif not b % a:
            print('factor')
        else:
            print('neither')
    else:
        break