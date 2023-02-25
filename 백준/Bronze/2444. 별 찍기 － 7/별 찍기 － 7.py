n = int(input())
for i in range(1, n*2):
    if i < n:
        print(' '*(n-i)+'*'*(i*2-1))
    else:
        print(' '*(i-n)+'*'*(4*n-2*i-1))