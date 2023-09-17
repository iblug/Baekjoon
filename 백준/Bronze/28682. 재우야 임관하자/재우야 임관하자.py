import sys
print = sys.stdout.write
n = int(input())
for _ in range(n):
    print('swimming ')
sys.stdout.flush()
s = input().split()
for e in s:
    if e == 'bowling':
        print('soccer ')
    else:
        print('bowling ')
sys.stdout.flush()