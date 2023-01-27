import sys
input = sys.stdin.readline

def check(i):
    while i < l:
        if a[i] == '(':
            i += 1
            i = check(i)
        elif a[i] == ')':
            return i+1
        else:
            i += 1
        if i == False:
            return False
    return False
    
n = int(input())
c = 'YES'
for _ in range(n):
    a = input().rstrip()
    l = len(a) # 배열의 길이
    i = 0
    while i < l:
        if a[i] == '(':
            i += 1
            i = check(i)
        elif a[i] == ')':
            i = False
            break
        else:
            i += 1
        if i == False:
            break
    if i == False:
        c = 'NO'
    else:
        c = 'YES'
    print(c)