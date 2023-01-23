n, m = map(int, input().split())
mat1=[list(map(int, input().split())) for _ in range(n)]
mat2=[list(map(int, input().split())) for _ in range(n)]

result = [[] for _ in range(n)]
for x in range(n):
    for y in range(m):
        result[x].append(mat1[x][y]+mat2[x][y])

for a in result:
    for b in range(m):
        print(a[b],end = ' ')
    print()