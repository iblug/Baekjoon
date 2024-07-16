a = input()
m = {'a', 'e', 'i', 'o', 'u'}
r = 0
for e in m:
    r += a.count(e)
print(r, r + a.count('y'))