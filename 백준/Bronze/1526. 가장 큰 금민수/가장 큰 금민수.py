n = int(input())

while True:
    n_ = str(n)
    n_ = n_.replace('7', '')
    n_ = n_.replace('4', '')
    if n_:
        n -= 1
    else:
        print(n)
        break