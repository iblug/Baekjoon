s = input()
d = set()
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        d.add(s[i:j])
print(len(d))