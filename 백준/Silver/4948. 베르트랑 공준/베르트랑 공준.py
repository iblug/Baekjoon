g = [1]*(123456*2+1)
g[0], g[1] = 0, 0
for i in range(2, int((123457*2)**0.5)+1):
    if g[i]:
        for j in range(i*2, 123456*2+1, i):
            g[j] = 0
while 1:
    a = int(input())
    if a == 0:
        break
    print(sum(g[a+1:2*a+1]))