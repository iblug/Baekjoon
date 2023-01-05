# https://www.acmicpc.net/problem/3190

n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)]
info = []

for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

l = int(input())

for _ in range(l):
    x, c = input().split()
    info.append((int(x),c))

d = 0
x1 = [0, 1, 0, -1]
y1 = [1, 0, -1, 0]
s = [1, 1]

for i in range(1, range(info[l][0] + 1)):
    s[0]


print(info)








'''
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
'''
'''
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L
'''
'''
10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
'''