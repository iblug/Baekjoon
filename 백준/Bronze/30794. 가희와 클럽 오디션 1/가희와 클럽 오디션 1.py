l, j = input().split()
match j:
    case 'miss':
        print(0)
    case 'bad':
        print(int(l) * 200)
    case 'cool':
        print(int(l) * 400)
    case 'great':
        print(int(l) * 600)
    case 'perfect':
        print(int(l) * 1000)