import sys

N = int(input())

result = [0] * 10001

for _ in range(N):
    x = sys.stdin.readline()
    result[int(x)] += 1
for i in range(1, 10001):
    for _ in range(result[i]):
        sys.stdout.write(str(i)+'\n')