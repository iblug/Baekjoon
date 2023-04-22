n = input()
for i in reversed(range(4)):
    r = ''
    for j in range(4):
        if int(n[j]) & 2**i:
            r += '*'
        else:
            r += '.'
        if j == 1:
            r += ' '
    print(' '.join(r))