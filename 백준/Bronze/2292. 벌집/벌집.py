data = int(input())
i = 1
while True:
    if data <= i * (i - 1) * 3 + 1:
        break
    i += 1

print(i)