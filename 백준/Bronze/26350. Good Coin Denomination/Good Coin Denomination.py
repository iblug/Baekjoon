for _ in range(int(input())) :
    N, *D = map(int, input().split())
    f = False
    for i in range(1, N) :
        if (D[i-1] << 1) > D[i] :
            break
    else:
        f = True
    print("Denominations:", *D)
    print(["Bad coin denominations!", "Good coin denominations!"][f], '\n')