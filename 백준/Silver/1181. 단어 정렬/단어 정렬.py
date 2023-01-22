import sys
input=sys.stdin.readline
N = int(input())
d=set(input().rstrip() for _ in range(N))
print('\n'.join(sorted(d,key=lambda x:(len(x),x))))