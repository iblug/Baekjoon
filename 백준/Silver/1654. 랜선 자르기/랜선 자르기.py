import sys
input = sys.stdin.readline

def bin(arr, start, end):
    mid = (end + start) // 2
    cnt = 0
    for i in arr:
        cnt += i // mid
    
    if cnt < n:
        end = mid - 1
        bin(arr, start, end)
    elif cnt >= n:
        result.append(mid)
        start = mid + 1
        if start > end:
            return True
        bin(arr, start, end)
    return True

k , n = map(int, input().split())
data = [int(input()) for _ in range(k)]
longest = max(data)
result = []
bin(data, 1, longest)
print(max(result))