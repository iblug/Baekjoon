N = int(input())
w = list(map(int, input().split()))
e = list(map(int, input().split()))

cnt = 0
ww = ee = 0
for i in range(N):
    ww += w[i]
    ee += e[i]
    if ww == ee:
        cnt = i +1 
print(cnt)