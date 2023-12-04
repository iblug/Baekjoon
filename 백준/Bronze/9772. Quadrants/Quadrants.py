import sys
input = sys.stdin.readline
while 1:
    a, b = map(float, input().split())
    if a * b:
        if a > 0:
            if b > 0:
                print('Q1')
            else:
                print('Q4')
        else:
            if b > 0:
                print('Q2')
            else:
                print('Q3')
    elif a == 0 and b == 0:
        print('AXIS')
        break
    else:
        print('AXIS')
