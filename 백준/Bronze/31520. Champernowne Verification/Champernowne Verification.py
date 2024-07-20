a = '123456789'
s = input()
if a[:len(s)] == s:
    print(len(s))
else:
    print(-1)