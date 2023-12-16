n = input()

a = list(input().split())
c = 0
for i in a:
    if i == n:
        c += 1
print(c)