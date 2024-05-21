n = int(input())
for i in range(1, n+1):
    if i%7 and i%11:
        print(i)
    elif i%7:
        print('Super!')
    elif i%11:
        print('Hurra!')
    else:
        print('Wiwat!')