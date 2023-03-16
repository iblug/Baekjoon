import sys
input = sys.stdin.readline

d = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while 1:
    c = 0
    s = input().rstrip()
    if s == '#':
        break
    for i in d:
        c += s.count(i)
    print(c)