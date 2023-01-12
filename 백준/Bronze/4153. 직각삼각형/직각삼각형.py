while True:
    x,y,z=sorted(map(int,input().split()))
    if x==y==z==0:
        break
    print(('wrong','right')[x*x+y*y==z*z])