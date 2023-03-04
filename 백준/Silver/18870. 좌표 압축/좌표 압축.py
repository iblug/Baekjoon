n = int(input())
d = list(map(int, input().split()))

s = sorted(set(d))
r = {x:i for i, x in enumerate(s)}

print(' '.join([str(r[i])for i in d]))