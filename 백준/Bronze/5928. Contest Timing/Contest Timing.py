d, h, m = map(int, input().split())
a = d*1440+h*60+m-16511
print([a,-1][a < 0])