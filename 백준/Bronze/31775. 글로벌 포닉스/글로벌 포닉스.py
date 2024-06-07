a = set()

for _ in range(3):
    s = input()
    a.add(s[0])

if a == {'l', 'k', 'p'}:
    print('GLOBAL')
else:
    print('PONIX')