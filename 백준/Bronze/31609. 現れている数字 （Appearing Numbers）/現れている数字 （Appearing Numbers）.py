f = [False] * 10
n = int(input())
a = list(map(int, input().split()))
for i in a:
    f[i] = True
for i in range(10):
    if f[i]:
        print(i)