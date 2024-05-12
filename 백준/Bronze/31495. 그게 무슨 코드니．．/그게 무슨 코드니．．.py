s = input()

if s.count('"') < 2 or len(s) < 3:
    print('CE')
elif s[0] == '"' and s[-1] == '"':
    print(s[1:-1])
else:
    print('CE')