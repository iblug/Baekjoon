t = int(input())
for _ in range(t):
    s = input()
    r = 0
    for a in s:
        if a == '(':
            r += 1
        elif a == ')':
            r -= 1
            if r < 0:
                print('NO')
                break
    else:
        if r == 0:
            print('YES')
        else:
            print('NO')