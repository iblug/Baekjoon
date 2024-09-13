import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p1, p2 = 0, 0
    r = int(input())
    for _ in range(r):
        r1, r2 = input().split()
        if r1 == r2:
            continue
        elif (r1 == 'S' and r2 == 'R') or (r1 == 'R' and r2 == 'P') or (r1 == 'P' and r2 == 'S'):
            p2 += 1
        else:
            p1 += 1
    if p1 > p2:
        print('Player 1')
    elif p1 < p2:
        print('Player 2')
    else:
        print('TIE')