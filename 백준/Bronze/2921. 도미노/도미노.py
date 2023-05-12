n = int(input())
s = 0
for i in range(n+1):
    for j in range(i+1):
        s += i+j
print(s)