import heapq
_,*d=open(0)
h=[]
for i in d:
 if i[0] == '0':
  if h:print(-heapq.heappop(h))
  else:print(0)
 else:heapq.heappush(h,-int(i))
