y = []
t = []
for _ in range(3):
    a, b, c = input().split()
    a = int(a)
    b = int(b[-2:])
    y.append(b)
    t.append((a, c))
ry = sorted(y)
rt = sorted(t, key=lambda x: x[0], reverse=True)
print(''.join(map(str, ry)))
print(''.join([p[1][0] for p in rt]))