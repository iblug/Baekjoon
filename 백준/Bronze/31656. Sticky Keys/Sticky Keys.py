s = input()
t = s[0]
r = t
for i in s[1:]:
    if i == t:
        continue
    else:
        t = i
        r += i
print(r)