e = ['a', 'e', 'i', 'o', 'u']
s = input()
r = 0
for i in e:
    r += s.count(i)
print(r)