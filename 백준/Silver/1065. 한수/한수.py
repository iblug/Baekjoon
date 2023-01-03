x = int(input())
def han(x):
    digits = list(map(int, str(x)))
    if len(digits) < 3:
        return True
    else:
        for i in range(len(digits)-2):
            if digits[i] - digits[i+1] != digits[i+1] - digits[i+2]:
                return False
            else:
                return True
    return False

c = 0
for x in range(1, x + 1):
    if han(x) == True:
        c += 1
print(c)