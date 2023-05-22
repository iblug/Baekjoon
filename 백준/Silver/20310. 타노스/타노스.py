s = list(map(int, list(input())))
n = len(s)
c1 = sum(s)
c0 = (n-c1)//2
c1 //= 2
r = [0]*(n//2)
re = set()
for i in range(n):
    if c1:
        if s[i] == 1:
            re.add(i)
            c1 -= 1
for i in reversed(range(n)):
    if c0:
        if s[i] == 0:
            re.add(i)
            c0 -= 1
a = [s[i] for i in range(n) if i not in re]
print(''.join(map(str, a)))