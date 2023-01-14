from itertools import combinations

n,m=map(int, input().split())
s=list(map(int, input().split()))

d=list(combinations(s, 3))
r=1e9

for i in d:
    if m>=sum(i):
        if r!=min(r,m-sum(i)):
            r=min(r,m-sum(i))
            p=sum(i)
print(p)