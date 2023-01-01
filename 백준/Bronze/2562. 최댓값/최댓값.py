a=[]
m=0
for i in range(9):
    a.append(int(input()))
    if a[i] > m:
        m = a[i]
        c = i+1
print(m, c, sep="\n")