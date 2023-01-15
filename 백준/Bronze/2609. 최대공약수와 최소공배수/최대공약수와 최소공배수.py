a, b = sorted(list(map(int, input().split())))
a1, b1 = a, b
while True:
    if b % a == 0:
        print(a)
        break
    b, a = a, b % a

print(b1*a1//a)