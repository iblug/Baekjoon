data = int(input())
i = 0

while True:
    if data <= i * (i - 1) * 3 + 1:
        break
    i += 1

if data == 1:
    print(1)
else:
    print(i)