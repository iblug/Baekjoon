s = input()
l = len(s)
new = ''
cnt = 0
for i in range(l):
    if s[i] == 'X':
        cnt += 1
    else:
        if cnt & 1:
            print(-1)
            exit()
        else:
            while cnt > 3:
                new += 'A'*4
                cnt -= 4
            if cnt == 2:
                new += 'BB'
            new += '.'
        cnt = 0
if cnt & 1:
    print(-1)
    exit()
while cnt > 3:
    new += 'A'*4
    cnt -= 4
if cnt == 2:
    new += 'BB'
print(new)