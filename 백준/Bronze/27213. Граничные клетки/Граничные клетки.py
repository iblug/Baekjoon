m = int(input())
n = int(input())
if m * n == 1:
    print(1)
elif m*n == n or m*n == m:
    print(m*n)
else:
    print((m+n)*2-4)