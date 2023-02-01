def fact(x):
    if x == 0 or x == 1:
        return 1
    return x * fact(x-1)

n = int(input())

m = fact(n)
cnt = 0

while m > 0:
    if m % 10 == 0:
        cnt += 1
        m = m // 10
    else:
        break

print(cnt)