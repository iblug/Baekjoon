import sys
input=sys.stdin.readline
r={}
for _ in range(int(input())):
 a=input().rstrip()
 r[a[:-6]]=a[-1]
print('\n'.join(sorted([i for i in r if r[i]=='r'],reverse=1)))