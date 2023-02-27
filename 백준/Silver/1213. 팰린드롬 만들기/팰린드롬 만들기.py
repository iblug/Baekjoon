from collections import Counter
d=Counter(input())
f = 0
c = ''
for k, v in d.items():
    if v%2 == 1:
        if not f:
            c = k
            f=1
        else:
            print("I'm Sorry Hansoo")
            exit()
    d[k]=v//2
d = dict(sorted(d.items()))
r = ''
for k, v in d.items():
    r += k*v
print(r+c+r[::-1])