a, b = map(int, input().split())
c, d = map(int, input().split())

min_ = min(a, c)
max_ = max(b, d)

g = [1]*(max_+1)
cnt1 = cnt2 = 0

for i in range(2, int(max_**0.5)+1):
    for j in range(min_, max_+1):
        if j == i:
            continue
        if g[j]:
            if j%i == 0:
                g[j] = 0

yt = set([i for i in range(a, b+1) if g[i]])
yj = set([i for i in range(c, d+1) if g[i]])
s = yt.union(yj)

yt_l = len(yt)
yj_l = len(yj)
s_l = len(s)

if s_l - yt_l > s_l - yj_l:
    print('yj')
elif s_l - yt_l < s_l - yj_l:
    print('yt')
else:
    if s_l-len(yt-yj)-len(yj-yt) & 1:
        print('yt')
    else:
        print('yj')