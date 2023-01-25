n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]
for i in a:
    r = 1
    for j in a:
        if i[0] < j[0] and i[1] < j[1]:
            r += 1
    print(r, end=' ')