S = input()
result = ''
for i in S:
    if i.islower():
        result += chr((ord(i)-84)%26+97)
    elif i.isupper():
        result += chr((ord(i)-52)%26+65)
    else:
        result += i
print(result)