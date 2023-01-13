n=int(input())
for i in range(1, n):
    s=r=i
    while i>0:
        s+=i%10
        i//=10
    if s == n:
        print(r)
        break
else:
    print(0)