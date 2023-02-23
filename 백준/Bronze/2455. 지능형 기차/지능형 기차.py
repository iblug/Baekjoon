cnt = 0
p = []
for _ in range(4):
    a, b = map(int, input().split())
    cnt += -a+b
    p.append(cnt)
print(max(p))