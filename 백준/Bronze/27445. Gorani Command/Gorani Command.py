import sys
input = sys.stdin.readline

n, m = map(int, input().split())

n_m = 51
for i in range(1, n):
    a = int(input())
    if a == 0:
        print(i,1)
        exit()
    if a < n_m:
        n_m = a
        n_mi = i
b = list(map(int, input().split()))
if b[0] == 0:
    print(n, 1)
    exit()
if b[0] < n_m:
    n_mi = n
m_mi = b.index(min(b))+1
print(n_mi, m_mi)