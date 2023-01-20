_,*n=open(0)
r={}
for j in n:
 r[j[:-7]]=j[-2]
print('\n'.join(sorted([i for i in r if r[i]=='r'],reverse=1)))