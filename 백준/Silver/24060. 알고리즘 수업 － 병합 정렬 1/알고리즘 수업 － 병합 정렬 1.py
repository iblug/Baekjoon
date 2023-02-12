def merge_sort(a,s,e):
    if s < e:
        m = (s+e)//2
        merge_sort(a,s,m)
        merge_sort(a,m+1,e)
        merge(a,s,m,e)

def merge(a,s,m,e):
    global cnt, ans
    i, j, t = s, m+1, 0
    while i <= m and j <= e:
        if a[i] <= a[j]:
            tmp[t] = a[i]
            i += 1
        else:
            tmp[t] = a[j]
            j += 1
        t += 1
    while i <= m:
        tmp[t] = a[i]
        t += 1
        i += 1
    while j <= e:
        tmp[t] = a[j]
        t += 1
        j += 1
    i , t = s, 0    
    while i <= e:
        a[i] = tmp[t]
        cnt += 1
        if cnt == k:
            ans = a[i]
        i += 1
        t += 1
n, k = map(int, input().split())
a = list(map(int, input().split()))
tmp = [0]*n
cnt = 0
ans = 0
merge_sort(a,0,n-1)
if ans:
    print(ans)
else:
    print(-1)