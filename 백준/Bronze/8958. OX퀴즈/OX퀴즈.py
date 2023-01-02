n = int(input())

for i in range(n):
    s = input()
    l = len(s)
    c = 0
    r = 0
    for j in range(l):
        if s[j] == 'O':
            c += 1
        else:
            c = 0
        r += c
    print(r)