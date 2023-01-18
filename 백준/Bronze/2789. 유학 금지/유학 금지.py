data = 'CAMBRIDGE'
a = input()

r = ''
for i in a:
    if i not in data:
        r += i
print(r)