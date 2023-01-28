def find_(arr, start, end):
    mid = (start + end) // 2
    cnt = 0
    for i in arr:
        if i > mid:
            cnt += i - mid
    if cnt < m:
        end = mid - 1
        find_(arr, start, end)
    elif cnt >= m:
        result.append(mid)
        start = mid + 1
        if start > end:
            return True
        find_(arr, start, end)
    return True

n, m = map(int, input().split())
data = list(map(int, input().split()))
result = []
find_(data,0,max(data))
print(max(result))