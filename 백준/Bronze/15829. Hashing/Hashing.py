l = int(input())
s = input()
r = 0
for i in range(l):
    r += (ord(s[i]) - 96) * 31**i
print(r)