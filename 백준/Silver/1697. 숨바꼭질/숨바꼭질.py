from collections import deque

n, k = map(int,input().split())
m = max(n, k)
g = [[i*2,i+1,i-1] for i in range(m+2)]
vi = [1e9] * (m+2)
visited = [False] * (m+2)
def bfs(x,k):
    q = deque([x])
    vi[x] = 0
    visited[x] = True
    while q:
        x = q.popleft()
        if x == k:
            return vi[x]
        for i in g[x]:
            if 0 <= i <= m+1:
                if not visited[i]:
                    visited[i] = True
                    vi[i] = min(vi[i],vi[x] + 1)
                    q.append(i)
print(bfs(n,k))