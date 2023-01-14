l = int(input())
s = input()
r = 0
for i in range(l):
    r += (ord(s[i]) - 96) * 31**i
    if r > 1234567891:
        r %= 123456789
print(r)