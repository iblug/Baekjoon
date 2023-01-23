import sys
input = sys.stdin.read
n,*a=map(int,input().split())
a.sort()
print('\n'.join(map(str,a)))