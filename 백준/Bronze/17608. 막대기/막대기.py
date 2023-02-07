import sys, heapq
input = sys.stdin.readline

n = int(input())

h = [int(input())]
for _ in range(n-1):
    a = int(input())
    while h and h[0] <= a:
        heapq.heappop(h)
    heapq.heappush(h, a)
    
print(len(h))    