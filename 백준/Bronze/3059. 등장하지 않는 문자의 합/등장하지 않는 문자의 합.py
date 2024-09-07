import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    f = list(range(65, 91))
    s = input().rsplit()
    for e in s[0]:
        f[ord(e) - 65] = 0
    print(sum(f))