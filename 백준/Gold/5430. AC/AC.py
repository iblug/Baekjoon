import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = input().rstrip().replace('RR','')
    n = int(input().rstrip())
    c = p.count('D')
    if c > n:
        input()
        print('error')
        continue
    x = input().rstrip().replace('[','').replace(']','').split(',')
    f = 0
    s = 0
    e = n
    for i in p:
        if i == 'R':
            f ^= 1
        else:
            if f:
                e -= 1
            else:
                s += 1
    if f:
        print(f'[{",".join(reversed(x[s:e]))}]')
    else:
        print(f'[{",".join(x[s:e])}]')