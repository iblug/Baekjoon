import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
d = list(map(int, input().split()))

s = sorted(set(d))
r = {x:i for i, x in enumerate(s)}

for i in d:
    print(str(r[i])+' ')