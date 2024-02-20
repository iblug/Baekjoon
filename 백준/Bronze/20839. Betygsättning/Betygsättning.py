a, c, e = map(int, input().split())
x, y, z = map(int, input().split())

if e <= z:
    if c <= y:
        if a <= x:
            print("A")
        elif a/2 <= x:
            print("B")
        else:
            print("C")
    elif c/2 <= y:
        print("D")
    else:
        print("E")