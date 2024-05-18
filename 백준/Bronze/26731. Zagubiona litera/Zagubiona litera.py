s = input()
a = [False] * 26

for e in s:
    a[ord(e) - ord('A')] = True

for i in range(26):
    if not a[i]:
        print(chr(i+ord('A')))