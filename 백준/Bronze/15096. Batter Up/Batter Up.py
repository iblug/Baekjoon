n = int(input())
l = list(map(int, input().split()))
r = 0
for i in l:
    if i < 0:
        n -= 1
    else:
        r += i
print(r/n)