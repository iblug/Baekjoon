n = int(input())
while n > 0:
    s = input().rstrip()
    t = ''
    for c in s:
        if c != t:
            print(c, end='')
            t = c
    print()
    n -= 1