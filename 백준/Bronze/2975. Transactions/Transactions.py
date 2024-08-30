import sys
input = sys.stdin.readline

while (True):
    s = input().rstrip()
    if s == '0 W 0':
        break
    a, b, c = s.split()
    a = int(a)
    c = int(c)
    if b == 'W':
        if a - c < -200:
            print('Not allowed')
        else:
            print(a - c)
    else:
        print(a + c)