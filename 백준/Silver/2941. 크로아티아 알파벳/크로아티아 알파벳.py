data = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
a = 0
for i in data:
    a += s.count(i)
print(len(s) - a)