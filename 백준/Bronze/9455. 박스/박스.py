import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m, n = map(int, input().split())
    data = [list(input().split()) for _ in range(m)]
    total = 0
    for n1 in range(n):
        cnt0 = cnt1 = 0
        sum_ = 0
        for m1 in range(m):
            if data[m1][n1] == '1':
                cnt1 += 1
            elif data[m1][n1] == '0':
                if cnt1 > 0:
                    sum_ += cnt1
        total += sum_
    print(total)