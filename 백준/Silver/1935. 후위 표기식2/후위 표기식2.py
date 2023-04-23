import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()
l = [int(input()) for _ in range(n)]
stack = []
for j in s:
    if 'A' <= j <= 'Z':
        stack.append(l[ord(j)-ord('A')])
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
print(f'{stack[0]:0.2f}')
