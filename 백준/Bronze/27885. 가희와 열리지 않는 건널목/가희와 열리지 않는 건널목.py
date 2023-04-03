r = [True]*86400
c, h = map(int, input().split())
for _ in range(c+h):
    a, b, d = map(int, input().split(':'))
    e = a*3600+b*60+d
    r[e:e+40]=[False]*40
print(sum(r))