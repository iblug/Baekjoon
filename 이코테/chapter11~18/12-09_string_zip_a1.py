s = input()
a = len(s)
for step in range(1, len(s) // 2 + 1):
    count = 1
    com = ""
    now = s[0:step]
    for i in range(step, len(s), step):
        if now == s[i: i + step]:
            count += 1
        else:
            com += str(count) + now if count >= 2 else now
            now = s[i: i + step]
            count = 1
    com += str(count) + now if count >= 2 else now

    a = min(a, len(com))

print(a)

'''
aabbaccc
ababcdcdababcdcd
abcabcdede
abcabcabcabcdededededede
xababcdcdababcdcd
aaaabbabbabb
'''
