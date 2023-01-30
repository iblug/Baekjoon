n = s = 0
for i in range(5):
    a = list(map(int, input().split()))
    s_ = sum(a)
    if s_ > s:
        s = s_
        n = i+1
print(n, s)