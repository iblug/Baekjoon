s = input()
i = 0
while i < len(s):
    print(s[i], end='')
    i += ord(s[i]) - ord('A') + 1