import sys

N = int(input())

result = [0] * 10001

for _ in range(N):
    result[int(sys.stdin.readline().rstrip())] += 1
for i in range(1, 10001):
    for _ in range(result[i]):
        sys.stdout.write(str(i)+'\n')