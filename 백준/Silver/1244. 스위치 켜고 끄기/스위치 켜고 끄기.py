import sys
input = sys.stdin.readline

def man(c):
    for cm in range(c, n, c+1):
        sw[cm] = (sw[cm] + 1)%2

def woman(c):
    sw[c] = (sw[c]+1)%2
    for cw in range(1, n//2+1):
        if c-cw < 0 or c+cw >= n:
            break
        if sw[c-cw] == sw[c+cw]:
            sw[c-cw] = (sw[c-cw]+1)%2
            sw[c+cw] = (sw[c+cw]+1)%2
        else:
            break

n = int(input())
sw = list(map(int, input().split()))

st = int(input())
for _ in range(st):
    g, c = map(int, input().split())
    if g == 1:
        man(c-1)
    elif g == 2:
        woman(c-1)
ic = 1
for i in range(n):
    print(sw[i], end=' ')
    ic += 1
    if ic > 20:
        print()
        ic = 1