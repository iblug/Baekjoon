s = input().replace(' ', '').split(':')
t = input().replace(' ', '').split(':')
a, b, c = map(int, s)
d, e, f = map(int, t)
ss = a*3600 + b*60 + c
tt = d*3600 + e*60 + f

if ss < tt:
    print(tt - ss)
else:
    print(tt - ss + 3600*24)
