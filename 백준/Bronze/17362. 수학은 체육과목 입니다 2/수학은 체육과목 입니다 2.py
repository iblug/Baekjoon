t = int(input()) % 8
if t == 1:
    print(1)
elif t == 0 or t == 2:
    print(2)
elif t == 3 or t == 7:
    print(3)
elif t == 4 or t == 6:
    print(4)
else:
    print(5)