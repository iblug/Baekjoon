s = input()

count = 0
temp = int(s[0])
result = 0
for i in range(len(s)):
    num = int(s[i])
    if temp != num:
        count += 1
        temp = num

result = (count + 1) // 2

print(result)