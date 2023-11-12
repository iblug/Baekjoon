import sys
input = sys.stdin.readline

while (1):
    s = input().rstrip().replace('i', '*').replace('I', '_').replace('e', 'i').replace('E', 'I').replace('*', 'e').replace('_', 'E')
    if s == '':
        break
    print(s)