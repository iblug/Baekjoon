import sys
input = sys.stdin.readline

score = [10, 8, 6, 5, 4, 3, 2, 1]
rank = []
for _ in range(8):
    M, SS, sss , T = input().rstrip().replace(':',' ').split()
    rank.append((int(M+SS+sss), T))
    
rank.sort()
R = 0
B = 0
i = 0
for t, T in rank:
    if T == 'R':
        R += score[i]
    else:
        B += score[i]
    i += 1

if R > B:
    print('Red')
else:
    print('Blue')