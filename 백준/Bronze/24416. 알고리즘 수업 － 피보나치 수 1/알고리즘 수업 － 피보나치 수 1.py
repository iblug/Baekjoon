def fibo(x):
    a, b = 0, 1
    for _ in range(x):
        a, b = b, a+b
    return a
n = int(input())
if n == 1 or n == 2:
    r = 1
else:
    r = n-2
print(fibo(n), r)