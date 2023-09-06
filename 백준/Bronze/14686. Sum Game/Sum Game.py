N = int(input())
w = [0] + list(map(int, input().split()))
e = [0] + list(map(int, input().split()))

cnt = 0
ww = ee = 0
for i in range(N+1):
    ww += w[i]
    ee += e[i]
    if ww == ee:
        cnt = i 
print(cnt)