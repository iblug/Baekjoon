n = int(input())
data = ['0', '1', '2', '3', '5', '6', '8', '9']

while True:
    n_ = str(n)
    for d in data:
        if d in n_:
            n -= 1
            break
    else:
        print(n)
        break