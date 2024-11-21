n = int(input())
s = input()
for i in range(n//2):
    if s[i] != s[n//2 + i]:
        print('No')
        break
else:
    print('Yes')