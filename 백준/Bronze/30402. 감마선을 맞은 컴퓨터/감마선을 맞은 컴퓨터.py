import sys
input = sys.stdin.readline

for i in range(15):
    b = input().split()
    if 'w' in b : 
        print('chunbae')
        break
    elif 'b' in b : 
        print('nabi')
        break
    elif 'g' in b : 
        print('yeongcheol')
        break