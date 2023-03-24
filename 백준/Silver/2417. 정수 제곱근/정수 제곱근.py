def f(s,e):
    if s > e:
        return s
    m = (s+e)//2
    if m**2 < n:
        return f(m+1, e)
    elif m**2 >= n:
        return f(s, m-1)
n = int(input())
print(f(0,n))