n, m = map(int, input().split())
data = []
for r in range(n):
    data.append(input())
result = []
for a in range(n-7):
    for b in range(m-7):
        cnt1 = cnt2 = 0
        for c in range(a, a+8):
            for d in range(b, b+8):
                if (c+d) % 2 == 0:
                    if data[c][d] == 'W':
                        cnt1 += 1
                    elif data[c][d] == 'B':
                        cnt2 += 1
                elif (c+d) % 2 == 1:
                    if data[c][d] == 'B':
                        cnt1 += 1
                    elif data[c][d] == 'W':
                        cnt2 += 1
        result.append(cnt1)
        result.append(cnt2)
print(min(result))