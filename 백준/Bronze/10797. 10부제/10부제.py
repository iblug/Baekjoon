n = input()
s = input().replace(' ','')
c = 0
for i in s:
    if  i == n:
        c += 1
print(c)