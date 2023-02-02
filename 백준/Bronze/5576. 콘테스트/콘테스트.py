import sys,heapq
input = sys.stdin.readline

sum1, sum2 = [], []

for _ in range(10):
    sum1.append(int(input()))
for _ in range(10):
    sum2.append(int(input()))
result1 = sum(sorted(sum1)[-3:])
result2 = sum(sorted(sum2)[-3:])
print(result1, result2)