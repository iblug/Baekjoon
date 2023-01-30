import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().split())

h = []

for _ in range(n):
    a, g, s, b = list(map(int, input().split()))
    heapq.heappush(h, (-g, -s, -b, a))
    if a == k:
        gk , sk, bk = g, s, b

mg, ms, mb = [], [], []

while h:
    hp = heapq.heappop(h)
    if hp[3] == k:
        break
    if -hp[0] > gk:
        mg.append(hp)
    elif -hp[1] > sk:
        ms.append(hp)
    elif -hp[2] > bk:
        mb.append(hp)
        
print(sum(map(len, (mg, ms, mb)))+1)