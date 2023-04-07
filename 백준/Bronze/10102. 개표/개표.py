n = int(input())
s = input()
a = s.count('A')
b = n-a
if a > b:
    print('A')
elif b > a:
    print('B')
else:
    print('Tie')