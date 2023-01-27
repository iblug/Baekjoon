import heapq
import sys
input = sys.stdin.readline
h = []
n = int(input())
for _ in range(n):
    c = int(input())
    if c != 0:
        heapq.heappush(h, c)
    else:
        if h:
            print(heapq.heappop(h))
        else:
            print(0)