n = int(input())
s = 0
for i in range(1, n-1):
    s += i * (n-i-1)
print(s, 3)