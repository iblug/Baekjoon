import sys
input = sys.stdin.readline

N = int(input())
A = input().split()
B = input().split()
M = int(input())
C = input().split()[::-1]
for i in range(N):
    if A[i] == '0':
        C.append(B[i])
print(' '.join(C[-M:][::-1]))