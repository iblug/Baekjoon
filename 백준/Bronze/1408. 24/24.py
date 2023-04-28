n = list(map(int, input().split(':')))
m = list(map(int, input().split(':')))

r = [0]*3
r[0] = m[0] - n[0]
r[1] = m[1] - n[1]
r[2] = m[2] - n[2]
if r[2] < 0:
    r[2] += 60
    r[1] -= 1
if r[1] < 0:
    r[1] += 60
    r[0] -= 1
if r[0] < 0:
    r[0] += 24

for i in range(3):
    r[i] = str(r[i])
    if len(r[i]) < 2:
        r[i] = '0' + r[i]
print(':'.join(r))
