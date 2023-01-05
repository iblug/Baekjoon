s = input().upper()
result = {}
for j in s:
    if j not in result.keys():
        result[j] = 0
    result[j] += 1
M = max(result.values())
c = 0
r = ''
for k, v in result.items():
    if M == v:
        c += 1
        r = k
if c > 1:
    print('?')
else:
    print(r)