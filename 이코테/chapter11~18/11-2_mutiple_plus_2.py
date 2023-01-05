s = input()

result = int(s[0])

for i in range(1, len(s)):
    a = int(s[i])
    if result <= 1 or a <= 1:
        result += a
    else:
        result *= a

print(result)