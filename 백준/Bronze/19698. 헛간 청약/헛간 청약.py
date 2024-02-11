n, w, h, l = map(int, input().split())
a = (w//l) * (h//l)
print(n if a > n else a)