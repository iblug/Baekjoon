s = input()
cnt1 = s.count(':-)')
cnt2 = s.count(':-(')

if cnt1 == 0 and cnt2 == 0:
    print('none')
elif cnt1 == cnt2:
    print('unsure')
elif cnt1 > cnt2:
    print('happy')
else:
    print('sad')