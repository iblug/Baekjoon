import sys
input = sys.stdin.readline

f = False
for i in range(1, 6):
    s = input()
    if s.count('FBI'):
        print(i, end=' ')
        f = True
if not f:
    print('HE GOT AWAY!')