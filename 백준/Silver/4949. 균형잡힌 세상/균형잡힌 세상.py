import sys
input = sys.stdin.readline
def check1(i):
    while i < l:
        if a[i] == '(':
            i += 1
            i = check1(i)
        elif a[i] == ')':
            return i+1
        elif a[i] == '[':
            i += 1
            i = check2(i)
        elif a[i] == ']':
            break
        else:
            i += 1
        if i == False:
            return False
    return False

def check2(i):
    while i < l:
        if a[i] == '(':
            i += 1
            i = check1(i)
        elif a[i] == ']':
            return i+1
        elif a[i] == '[':
            i += 1
            i = check2(i)
        elif a[i] == ')':
            break
        else:
            i += 1
        if i == False:
            return False
    return False

while True:
    a = input().rstrip()
    if a == '.':
        break
    c = True
    l = len(a)
    i = 0
    while i < l:
        if a[i] == '(':
            i += 1
            i = check1(i)
        elif a[i] == '[':
            i += 1
            i = check2(i)
        elif a[i] == ')' or a[i] == ']':
            i = False
        else:
            i += 1
        if i == False:
            break
    if i == False:
        print('no')
    else:
        print('yes')