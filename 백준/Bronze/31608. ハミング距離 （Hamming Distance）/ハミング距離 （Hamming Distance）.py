n = int(input())
s = input()
t = input()

r = 0
for i in range(n):
    if s[i] == t[i]:
        r += 1
print(n-r)