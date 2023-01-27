import sys, heapq
from collections import Counter
input = sys.stdin.readline

n = int(input())
h = []
most_list = []
for _ in range(n):
    heapq.heappush(h,int(input()))
most_temp = Counter(h).most_common()
most_cnt = most_temp[0][1]
for i in most_temp:
    if i[1] == most_cnt:
        heapq.heappush(most_list, i[0])
    else:
        break
if len(most_list) > 1:
    heapq.heappop(most_list)
    most_ = heapq.heappop(most_list)
else:
    most_ = heapq.heappop(most_list)
print(round(sum(h)/n))
print(heapq.nsmallest(n//2+1,h)[-1])
print(most_)
print(heapq.nlargest(1,h)[0]-heapq.nsmallest(1,h)[0])