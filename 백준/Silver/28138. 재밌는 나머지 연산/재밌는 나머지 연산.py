N, R = map(int, input().split())
a = N - R
t = set()
for i in range(1, int(a**0.5)+1):
    if a % i == 0:
        if i > R:
            t.add(i)
        if a//i > R:
            t.add(a//i)
print(sum(t))