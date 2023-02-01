import sys
input = sys.stdin.readline

def act(command, num):
    if command == 'add':
        s.add(num)
    if command == 'remove':
        if num in s:
            s.remove(num)
    if command == 'check':
        if num in s:
            print(1)
        else:
            print(0)
    if command == 'toggle':
        if num in s:
            act('remove', num)
        else:
            act('add', num)
    if command == 'all':
        for i in range(1, 21):
            s.add(i)
    if command == 'empty':
        s.clear()

n = int(input())

s = set()
for _ in range(n):
    command, *num = input().split()

    if num:
        num = int(num[0])

    act(command,num)