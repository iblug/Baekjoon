s = int(input())
a = int(input())
b = int(input())

if s > a:
    print(250 + ((s-a+b-1)//b) * 100)
else:
    print(250)