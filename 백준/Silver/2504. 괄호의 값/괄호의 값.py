import sys

s = list(input())[::-1]
def check(c):
    r = 0
    while s:
        a = s.pop()
        if a == '(' or a == '[':
            r += check(a)
        elif c == '(' and a == ')':
            return 2*max(1, r)
        elif c == '[' and a == ']':
            return 3*max(1, r)
    print(0)
    sys.exit()
answer = 0
while s:
    answer += check(s.pop())
print(answer)
