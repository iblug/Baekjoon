s = input().split('-')
r = sum(map(int,s[0].split('+')))
for e in s[1:]:
    r -= sum(map(int, e.split('+')))
print(r)