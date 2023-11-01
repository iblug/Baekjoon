a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = a[0] * 3 + a[1] * 20 + a[2] *120
d = b[0] * 3 + b[1] * 20 + b[2] *120
if c > d:
    print('Max')
elif d > c:
    print('Mel')
else:
    print('Draw')