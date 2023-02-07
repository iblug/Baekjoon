import sys, heapq
input = sys.stdin.readline

n = int(input())

h = [int(input())]
for _ in range(n-1):
    a = int(input())
    while h[0] <= a:
        heapq.heappop(h)
        if not h:
            break
    heapq.heappush(h, a)
print(len(h))