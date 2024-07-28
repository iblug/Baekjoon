input()
s = input()
a = s[0]
for i in s[1:]:
    if i != a:
        print('No')
        break
else:
    print('Yes')