import sys
input = sys.stdin.readline
print = sys.stdout.write
n, m, k = map(int, input().split())

if k < n+m-1:
    print('NO')
    exit()

print('YES\n')
for j in range(1, n+1):
    print(' '.join(map(str, range(j, m+j))))
    print('\n')
