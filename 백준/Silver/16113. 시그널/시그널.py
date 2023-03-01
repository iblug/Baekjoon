n = int(input())
s = input()
p = n//5

a = ''
i = 0
while i < p:
    if s[i] == '.':
        i += 1
        continue
    if s[i+3*p] == '#':
        if s[i+p] == '#':
            if i == p - 1:
                a += '1'
                break
            if s[i+1] == '.':
                t = '1'
            else:
                if s[i+2+p] == '.':
                    t = '6'
                elif s[i+1+2*p] == '#':
                    t = '8'
                else:
                    t = '0'
        else:
            t = '2'
    else:
        if s[i+1] == '.':
            t = '4'
        elif s[i+2*p] == '.':
            t = '7'
        elif s[i+2+p] == '.':
            t = '5'
        elif s[i+p] == '.':
            t = '3'
        else:
            t = '9'
    a += t
    if t == '1':
        i += 2
    else:
        i += 4
print(a)