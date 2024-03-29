import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()
l = [int(input()) for _ in range(n)]
stack = []
for j in s:
    if j.isalpha():
        stack.append(l[ord(j)-65])
    else:
        a = stack.pop()
        if j == '+':
            stack.append(stack.pop()+a)
        elif j == '-':
            stack.append(stack.pop()-a)
        elif j == '*':
            stack.append(stack.pop()*a)
        elif j == '/':
            stack.append(stack.pop()/a)
print('%.2f' %stack[0])
