s = input()

cnt1 = cnt2 = 0
i = 0
while True:
    if len(s) < 3:
        break
    if s[i:i+3] == ':-)':
        cnt1 += 1
    elif s[i:i+3] == ':-(':
        cnt2 += 1
    i += 1
    if i > len(s)-3:
        break
        
if cnt1 == 0 and cnt2 == 0:
    print('none')
elif cnt1 == cnt2:
    print('unsure')
elif cnt1 > cnt2:
    print('happy')
else:
    print('sad')