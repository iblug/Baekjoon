n = int(input())
d = list(map(int, input().split()))
r = [0]*n
visited = [0]*n
for i, v in enumerate(d, 1):
    cnt = 0
    for e in range(n):
        if cnt == v and not visited[e]:
            r[e] = i
            visited[e] = 1
            break
        if r[e] == 0:
            cnt += 1
print(' '.join(map(str, r)))