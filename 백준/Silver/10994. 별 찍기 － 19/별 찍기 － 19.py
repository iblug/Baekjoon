def star(l):
    for i in range(l-1):
        star1(i)
        star2(i)
    print('* '*(l-1)+'*'+' *'*(l-1))
    for i in reversed(range(l-1)):
        star2(i)
        star1(i)

def star1(l):
    print('* '*l + '*'*((n-l-1)*4+1)+' *'*l)

def star2(l):
    print('* '*(l+1)+' '*((n-l-2)*4+1)+' *'*(l+1))

n = int(input())
star(n)