data = [0 for _ in range(10001)]
def d(x):
    r = x
    while x > 0:
        r += x%10
        x //= 10
    return int(r)

for i in range(1, 10001):
    c = d(i)
    if c <= 10000:
        data[c] = 1
for i in range(1, 10001):
    if data[i] != 1:
        print(i)