m = int(input())
n = int(input())

r = []
for i in range(m, n+1):
    if i**0.5 == int(i**0.5):
        r.append(i)
if r:
    print(sum(r))
    print(r[0])
else:
    print(-1)