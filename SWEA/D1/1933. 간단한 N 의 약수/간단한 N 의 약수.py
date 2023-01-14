N=int(input())
print(*[n for n in range(1,N+1) if N%n==0])