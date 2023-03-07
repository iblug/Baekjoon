x, y, w, s = map(int, input().split())

if 2*w <= s:
    result = (x+y)*w
elif w > s:
    min_ = min(x, y)
    t = abs(x - y)
    if t & 1:
        result = (min_+t-1)*s+w
    else:
        result = (min_+t)*s
else:
    min_ = min(x, y)
    t = abs(x - y)
    result = (min_)*s+t*w
print(result)