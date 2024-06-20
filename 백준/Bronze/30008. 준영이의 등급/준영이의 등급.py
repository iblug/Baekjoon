n, k = map(int, input().split())
g = list(map(int, input().split()))
for e in g:
    d = e * 100 // n
    if d <= 4:
        print(1, end=' ')
    elif d <= 11:
        print(2, end=' ')
    elif d <= 23:
        print(3, end=' ')
    elif d <= 40:
        print(4, end=' ')
    elif d <= 60:
        print(5, end=' ')
    elif d <= 77:
        print(6, end=' ')
    elif d <= 89:
        print(7, end=' ')
    elif d <= 96:
        print(8, end=' ')
    else:
        print(9, end=' ')