import sys
input = sys.stdin.readline

n = int(input())
a_min = 0
a_max = 1e9
n_min = ''
n_max = ''
for _ in range(n):
    name, d, m, y = input().split()
    if len(m) == 1:
        m = '0'+m
    if len(d) == 1:
        d = '0'+d
    age = int(y+m+d)
    if age > a_min:
        a_min = age
        n_min = name
    if age < a_max:
        a_max = age
        n_max = name
print(n_min, n_max, sep='\n')