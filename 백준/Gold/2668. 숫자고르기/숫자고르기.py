import sys
input = sys.stdin.readline

def dfs(x,d):
    s = [(x,d)]
    v[x] = True
    while s:
        x, d = s.pop()
        d.append(x)
        for j in g[x]:
            if j not in d:
                v[j] = True
                s.append((j, d.copy()))
            else:
                r.append(d)
                return

n = int(input())
g = [[] for _ in range(n+1)]
v = [False]*(n+1)
for i in range(1, n+1):
    a = int(input())
    g[a].append(i)

r = []
for i in range(1, n+1):
    if not v[i]:
        dfs(i,[])
result = sum(r,[])
result.sort()
print(len(result))
print('\n'.join(map(str,result)))