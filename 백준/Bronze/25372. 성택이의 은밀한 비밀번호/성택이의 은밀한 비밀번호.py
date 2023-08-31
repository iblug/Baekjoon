import sys
input = sys.stdin.readline

for _ in range(int(input())):
    if  10 > len(input().rstrip()) > 5 :
        print('yes')
    else:
        print('no')