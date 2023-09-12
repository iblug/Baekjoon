import sys
input = sys.stdin.readline

n = int(input())
c = [tuple(map(int, input().split())) for _ in range(n)]
c.sort(key=lambda x:(x[1], x[0]))
cnt = 1
e = c[0][1]

for i in c[1:]:
    if i[0] >= e:
        cnt += 1
        e = i[1]
print(cnt)