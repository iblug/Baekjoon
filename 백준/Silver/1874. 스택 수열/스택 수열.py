import sys
input = sys.stdin.readline

n = int(input())
stack = []
result = []
i = 1
for _ in range(n):
    now = int(input())
    while now >= i:
        stack.append(i)
        result.append('+')
        i += 1
    if stack[-1] == now:
        stack.pop()
        result.append('-')    
    else:
        print('NO')
        exit()
print('\n'.join(result))
