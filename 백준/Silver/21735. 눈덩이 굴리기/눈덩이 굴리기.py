def dfs(i, s, m):
    if not m or i == n:
        r.append(s)
        return
    if (g:=i+1) <= n:
        dfs(g, s+a[g], m-1)
    if (j:=i+2) <= n:
        dfs(j,s//2 + a[j],m-1)
    
n, m = map(int, input().split())
a = [0]+list(map(int, input().split()))
r = []
dfs(0,1,m)
print(max(r))