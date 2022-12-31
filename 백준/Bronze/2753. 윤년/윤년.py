y=int(input())
print(+(y%400<1,y%4<1)[y%100>0])