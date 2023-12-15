import sys
input = sys.stdin.readline

while 1:
    n = int(input())
    if n == 0:
        break
    if n % 42:
        print('TENTE NOVAMENTE')
    else:
        print('PREMIADO')