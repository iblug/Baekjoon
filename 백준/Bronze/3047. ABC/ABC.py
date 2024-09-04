l = sorted(map(int, input().split()))
s = input()
for e in s:
    print(l[ord(e)-68], end=' ')