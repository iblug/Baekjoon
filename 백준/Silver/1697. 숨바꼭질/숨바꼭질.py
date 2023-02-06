from collections import deque


n, k = map(int,input().split())
m = max(n, k)
g = [[i*2,i+1,i-1] for i in range(m+2)]
vi = [1e9] * (m+2)
def bfs(x,k):
    q = deque([x])
    vi[x] = 0
    while q:
        x = q.popleft()
        if x == k:
            return vi[x]
        for i in g[x]:
            if 0 <= i <= m+1:
                if vi[i] == 1e9:
                    vi[i] = min(vi[i],vi[x] + 1)
                    q.append(i)
print(bfs(n,k))