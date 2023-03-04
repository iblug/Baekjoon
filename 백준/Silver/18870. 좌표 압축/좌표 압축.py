import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
d = list(map(int, input().split()))

s = sorted(set(d))
r = {}
for i in range(len(s)):
    r[s[i]] = i

for i in d:
    print(str(r[i])+' ')