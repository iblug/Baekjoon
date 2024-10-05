l = ['P', 'E', 'R']

s = input()
r = 0
for i in range(len(s)):
    if s[i] != l[i%3]:
        r += 1
print(r)