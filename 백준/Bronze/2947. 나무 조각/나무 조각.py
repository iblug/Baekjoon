s = list(map(int, input().split()))
while True:
    for i in range(4):
        if s[i] > s[i+1]:
            s[i], s[i+1] = s[i+1], s[i]
            print(*s)
    if s == sorted(s):
        break