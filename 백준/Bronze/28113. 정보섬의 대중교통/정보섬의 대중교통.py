n, a, b = map(int, input().split())

if a < b:
    print('Bus')
elif n > b:
    print('Bus')
elif b == a:
    print('Anything')
else:
    print('Subway')