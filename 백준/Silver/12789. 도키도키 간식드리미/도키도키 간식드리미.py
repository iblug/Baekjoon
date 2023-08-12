from collections import deque

n = int(input())
d = deque(list(map(int, input().split())))

s = deque()
i = 1
while i <= n:
    if d:
        a = d[0]
        if a == i:
            d.popleft()
            i += 1
        elif s:
            b = s[-1]
            if b == i:
                s.pop()
                i += 1
            else:
                s.append(d.popleft())
        else:
            s.append(d.popleft())
    elif s:
        b = s[-1]
        if b == i:
            s.pop()
            i += 1
        else:
            print('Sad')
            break
else:
    print('Nice')