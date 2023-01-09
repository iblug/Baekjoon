s = input()

count = 0
temp = int(s[0])
result = 0
for i in range(len(s)):
    num = int(s[i])
    if temp != num:
        count += 1
        temp = num

if count % 2 == 0:
    result = count // 2
else:
    result = (count // 2) + 1

print(result)