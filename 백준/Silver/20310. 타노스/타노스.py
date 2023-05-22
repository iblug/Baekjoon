s = list(map(int, list(input())))
n = len(s)
c1 = sum(s)
c0 = (n-c1)//2
c1 //= 2
r = set()
for i, v in enumerate(s):
    if c1 and s[i]:
        r.add(i)
        c1 -= 1
for i, v in reversed(list(enumerate(s))):
    if c0 and not s[i]:
        r.add(i)
        c0 -= 1
a = (s[i] for i in range(n) if i not in r)
print(''.join(map(str, a)))