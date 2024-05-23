n = int(input())
print(chr((n-1)%8+ord('a')), (n-1)//8+1, sep='')