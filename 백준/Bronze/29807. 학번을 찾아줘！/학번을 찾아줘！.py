n = int(input())
d = list(map(int, input().split()))
s = [0] * 5
for i in range(n):
    s[i] = d[i]
r = 0

if s[0] > s[2]:
    r += (s[0] - s[2]) * 508
else:
    r += (s[2] - s[0]) * 108

if s[1] > s[3]:
    r += (s[1] - s[3]) * 212
else:
    r += (s[3] - s[1]) * 305
r += s[4] * 707

print(r*4763)