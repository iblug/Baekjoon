n = int(input())
s = input()
r = 1
a = 0
for i in s:
    if i == 'L':
        r = max(r-1, 1)
    else:
        r = min(r+1, 3)
        if r == 3:
            a += 1
print(a)