import sys
input = sys.stdin.readline
import heapq

h = []
n = int(input())
for _ in range(n):
    c = int(input())
    if c != 0:
        heapq.heappush(h, (abs(c), c))
    else:
        if h:
            print(heapq.heappop(h)[1])
        else:
            print(0)
