n = input()
a = [0]*26
for i in n:
    a[ord(i) - ord('a')] += 1
print(' '.join(map(str, a)))