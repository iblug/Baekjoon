input()
l = list(map(int, input().split()))
a = l[0]
r = 0
for i in l:
    if i > a:
        r += 1
    a = i
print(r)