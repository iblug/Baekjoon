import sys
input = sys.stdin.readline

t = 0
while 1:
    s = input().rstrip()
    
    t += 1
    c = 0
    d = []
    if s[0] == '-':
        break
    for i in s:
        if i == '}':
            if d and d[-1] == '{':
                d.pop()
            else:
                d.append(i)
        else:
            d.append(i)
    while d:
        a = d.pop()
        b = d.pop()
        if a == b:
            c+=1
        else:
            c+=2
    print(f'{t}. {c}')