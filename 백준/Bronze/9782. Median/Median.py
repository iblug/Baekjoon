import sys
input = sys.stdin.readline

t = 0
while 1:
    t += 1
    a = list(map(int, input().split()))
    n = a[0]
    if n == 0:
        break
    if n % 2:
        print(f'Case {t}: {a[(n+1) // 2]:.1f}')
    else:
        print(f'Case {t}: {(a[n//2] + a[n//2 + 1])/2}')