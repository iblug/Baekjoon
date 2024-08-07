input()
s = input()
x , y = 0, 0
for e in s:
    if e == 'N':
        y += 1
    elif e == 'E':
        x += 1
    elif e == 'S':
        y -= 1
    else:
        x -= 1
print(abs(x)+abs(y))