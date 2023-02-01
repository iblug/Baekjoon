import sys
input = sys.stdin.readline

n, m = map(int, input().split())

h = set(input().rstrip() for _ in range(n))
s = set(input().rstrip() for _ in range(m))

hs = sorted(h & s)
print(len(hs),*hs,sep='\n')