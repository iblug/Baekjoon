b1 = [[0], [0, 0, 0, 0]]
b2 = [[0, 0]]
b3 = [[0, 0, 1], [1, 0]]
b4 = [[1, 0, 0], [0, 1]]
b5 = [[0, 0, 0], [0, 1], [1, 0, 1], [1, 0]]
b6 = [[0, 0, 0], [0, 0], [0, 1, 1], [2, 0]]
b7 = [[0, 0, 0], [0, 2], [1, 1, 0], [0, 0]]

bs = [0, b1, b2, b3, b4, b5, b6, b7]

C, P = map(int, input().split())
g = list(map(int, input().split()))

c = 0
for i in bs[P]:
    l = len(i)
    if C < l:
        continue
    for j in range(C-l+1):
        r = g[j:j+l][0] - i[0]
        for k in range(1, l):
            if g[j:j+l][k] - i[k] != r:
                break
        else:
            c += 1
print(c)