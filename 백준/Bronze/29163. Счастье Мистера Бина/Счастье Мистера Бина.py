n = int(input())
a = list(map(int, input().split()))
r = 0
for e in a:
    if e % 2 == 0:
        r += 1
        if r > n//2:
            print('Happy')
            break
else:
    print('Sad')