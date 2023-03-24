def f(s, e):
    if s > e:
        return e
    mid = (s+e)//2
    t = 0
    for i in b:
        if i > mid:
            t += mid
        else:
            t += i
    if t > m:
        return f(s,mid-1)
    else:
        return f(mid+1, e)
n = int(input())
b = list(map(int, input().split()))
m = int(input())

r = [0]
print(f(0, max(b)))