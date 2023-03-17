def per(lst):
    if len(lst) == m:
        print(' '.join(lst))
        return
    for i in range(n):
        lst.append(arr[i])
        per(lst)
        lst.pop()
n, m = map(int, input().split())
arr = list(map(str, range(1, n+1)))
per([])