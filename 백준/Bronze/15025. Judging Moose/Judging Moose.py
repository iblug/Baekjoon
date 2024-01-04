a, b = map(int, input().split())

if a == b:
    if a == 0:
        print('Not a moose')
    else:
        print(f'Even {a*2}')
else:
    if a > b:
        print(f'Odd {a*2}')
    else:
        print(f'Odd {b*2}')