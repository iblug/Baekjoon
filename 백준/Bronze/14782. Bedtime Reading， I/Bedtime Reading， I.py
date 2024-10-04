n = int (input())
r = 0
for i in range(1, int(n**0.5 + 1)):
    if not n%i:
        if n**0.5 == i:
            r += i
        else:
            r += i + n//i
print(r)