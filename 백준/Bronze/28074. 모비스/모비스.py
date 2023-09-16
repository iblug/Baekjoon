d = ['M', 'B', 'O', 'I', 'S']
s = input()
f = 1
for i in d:
    if i not in s:
        f = 0
if f:
    print('YES')
else:
    print('NO')