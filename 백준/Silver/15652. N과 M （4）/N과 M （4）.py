def f(arr:list, r:int):
    arr = sorted(arr)
    def g(c:list) -> None:
        if len(c) == r:
            print(*c)
            return
        start = arr.index(c[-1]) if c else 0
        for i in range(start, n):
            c.append(arr[i])
            g(c)
            c.pop()
    g([])

n, m = map(int, input().split())
lst = list(range(1, n+1))
f(lst, m)