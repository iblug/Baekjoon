s = input()
if len(s) < 3:
    print(sum(map(int, s)))
elif len(s) == 3:
    if s[1] == '0':
        print(10+int(s[2]))
    else:
        print(int(s[0])+10)
else:
    print(20)