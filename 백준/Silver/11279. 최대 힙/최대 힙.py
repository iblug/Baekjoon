import sys, heapq
input = sys.stdin.readline

n = int(input())
h = []
for _ in range(n):
    i = int(input())
    if i == 0:
        if h:
            print(-heapq.heappop(h))
        else:
            print(0)
    else:
        heapq.heappush(h, -i)