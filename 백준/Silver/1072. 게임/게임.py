def check(mid) -> bool:
    return (y+mid)*100//(x+mid) >= now + 1

x, y = map(int, input().split())

now = y*100//x
if now < 99:
    s = 0
    e = int(1e9)
    while s + 1 < e:
        mid = (s+e) // 2
        if check(mid):
            e = mid
        else:
            s = mid
    print(e)
else:
    print(-1)