input()
s = input()
r = 0
for i in s:
    if i == 'i' or i == 'j':
        r += 2
    else:
        r += 1
print(r)