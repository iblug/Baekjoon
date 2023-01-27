import heapq
def m(x):
    return -int(x)
h = list(map(m, input().split()))
heapq.heapify(h)
heapq.heappop(h)
print(-heapq.heappop(h))