def dfs(i, s, m):
    if not m or i == n:
        r.append(s)
        return
    if (g:=i+1) <= n:
        s+=a[g]
        dfs(g, s, m-1)
        s-=a[g]
    if (j:=i+2) <= n:
        t = s
        s = s//2 + a[j]
        dfs(j,s,m-1)
        s = t
    
n, m = map(int, input().split())
a = [0]+list(map(int, input().split()))
r = []
dfs(0,1,m)
print(max(r))