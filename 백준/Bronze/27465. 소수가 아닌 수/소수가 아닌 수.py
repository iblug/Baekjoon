n = int(input())
if n < 4:
    print(4)
else:
    if n&1:
        print(n+1)
    else:
        print(n)