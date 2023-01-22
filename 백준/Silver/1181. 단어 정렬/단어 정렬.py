import sys
input = sys.stdin.readline
d=set(input().rstrip() for _ in range(int(input())))
print(*sorted(d,key=lambda x:(len(x),x)),sep='\n')