s = 0
for i in range(3, 0, -1):
    s += int(input()) * i
for i in range(3, 0, -1):
    s -= int(input()) * i
if s > 0:
    print('A')
elif s < 0:
    print('B')
else:
    print('T')