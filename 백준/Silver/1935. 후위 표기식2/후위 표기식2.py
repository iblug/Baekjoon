import sys
input = sys.stdin.readline

o = ('+', '-', '*', '/')
n = int(input())
s = input().rstrip()
l = [int(input()) for _ in range(n)]
stack = []
for j in s:
    if j in o:
        a = stack.pop()
        if j == '+':
            stack.append(stack.pop()+a)
        elif j == '-':
            stack.append(stack.pop()-a)
        elif j == '*':
            stack.append(stack.pop()*a)
        elif j == '/':
            stack.append(stack.pop()/a)
    else:
        stack.append(l[ord(j)-ord('A')])
print(f'{stack[0]:0.2f}')