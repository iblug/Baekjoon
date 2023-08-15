import sys
i=sys.stdin.readline
N=int(i())
A,B=[i().split() for _ in '  ']
M=int(i())
C=i().split()[::-1]
print(' '.join((C+[B[x] for x in range(N) if A[x]=='0'])[-M:][::-1]))