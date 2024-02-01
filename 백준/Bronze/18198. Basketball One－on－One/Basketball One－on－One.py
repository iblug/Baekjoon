a = b = i = 0
s = input()
while i < len(s):
    if s[i] == "A":
        a += int(s[i+1])
    else:
        b += int(s[i+1])
    i += 2
if a > b:
    print("A")
else:
    print("B")