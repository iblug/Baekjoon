import sys
input = sys.stdin.readline

l = ['G...', '.I.T', '..S.']

K = int(input())

for e in l :
    t = ''
    for j in range(len(e)) : 
        t += (e[j] * K)
    
    for k in range(K) : 
        print(t)