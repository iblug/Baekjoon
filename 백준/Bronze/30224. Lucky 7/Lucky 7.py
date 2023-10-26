n = input()
if '7' not in n:
    n = int(n)
    if n % 7:
        print(0)
    else:
        print(1)
else:
    n = int(n)
    if n % 7:
        print(2)
    else:
        print(3)