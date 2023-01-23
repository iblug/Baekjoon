import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
cnt = 0
for a in A:
    a -=B
    cnt += 1
    if a > 0:
        if a % C == 0:
            cnt += a//C
        else:
            cnt += a // C + 1
print(cnt)