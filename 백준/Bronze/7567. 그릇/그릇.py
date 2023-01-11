d = input()
t = d[0]
c = 5
for i in d[1:]:
    if t == i:
        c += 5
        t = i
    else:
        c += 10
        t = i
c += 5
print(c)