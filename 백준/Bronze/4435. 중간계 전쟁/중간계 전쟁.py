import sys
input = sys.stdin.readline

gan = [1, 2, 3, 3, 4, 10, 0]
sa = [1, 2, 2, 2, 3, 5, 10]

T = int(input())
for t in range(1, T+1):
    gs, ss = 0, 0
    g = list(map(int, input().split()))+[0]
    s = list(map(int, input().split()))
    for i in range(7):
        gs += gan[i] * g[i]
        ss += sa[i] * s[i]
    if gs > ss:
        print(f'Battle {t}: Good triumphs over Evil')
    elif gs < ss:
        print(f'Battle {t}: Evil eradicates all trace of Good')
    else:
        print(f'Battle {t}: No victor on this battle field')