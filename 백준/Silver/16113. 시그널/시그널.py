n=int(input())
s=input()
p=n//5
a=''
i=0
while i<p:
 if s[i]=='.':i+=1;continue
 if s[i+3*p]=='#':
  if s[i+p]=='.':t='2'
  elif i==p-1:a+='1';break
  elif s[i+1]=='.':t='1'
  elif s[i+1+2*p]=='.':t='0'
  elif s[i+2+p]=='.':t='6'
  else:t='8'
 else:
  if s[i+1]=='.':t='4'
  elif s[i+2*p]=='.':t='7'
  elif s[i+2+p]=='.':t='5'
  elif s[i+p]=='.':t='3'
  else:t='9'
 a+=t
 if t=='1':i+=2
 else:i+=4
print(a)