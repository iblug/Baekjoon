n = int(input())
if n > 5:
    print(0)
else:
    i = 0
    t = 1
    while 1:
        if i == n:
            break
        i += 1
        t = i*(t%10)
    print(t%10)