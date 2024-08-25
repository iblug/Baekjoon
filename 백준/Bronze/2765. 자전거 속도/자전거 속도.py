import sys, math
input = sys.stdin.readline

i = 0
while (True):
    i += 1
    r, o, t = map(float, input().split())
    if o == 0:
        break
    d = r/(12*5280)*3.1415927*o
    print(f'Trip #{i}: {d:.2f} {d*3600/t:.2f}')