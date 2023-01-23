import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
r = []
for a in A:
    if a > B:
        r.append(1 - (B-a)//C)
    else:
        r.append(1)
print(sum(r))