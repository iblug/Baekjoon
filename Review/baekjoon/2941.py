# https://www.acmicpc.net/problem/2941
# 크로아티아 알파벳

data = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
a = 0
for i in data:
    a += s.count(i)
print(len(s) - a)

# 구현
# replace 활용