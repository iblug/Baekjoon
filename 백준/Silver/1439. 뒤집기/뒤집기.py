data = input()

temp = data[0]
count = 0
result = 0

for num in data:
    if temp != num:
        temp = num
        count += 1

print((count + 1) // 2)