import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    data = {input().rstrip() for _ in range(n)}
    data1 = sorted(data, key=lambda x: len(x), reverse=True)
    f = 0
    for i in data1:
        for j in range(len(i)):
            if i[:j] in data:
                f = 1
                break
        if f:
            break
    if f:
        print('NO')
    else:
        print('YES')