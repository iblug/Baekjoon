n = int(input())
p = int(input())
a, b = 0, 1

if n >= 5:
    a = 500
if n >= 10:
    b = 0.9
if n >= 15:
    a = 2000
if n >= 20:
    b = 0.75
print(max(0, int(min(p-a, p*b))))