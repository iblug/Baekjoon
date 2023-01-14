# https://www.acmicpc.net/problem/2941
# 크로아티아 알파벳

import sys
sys.stdin = open('input.txt', 'r')

data = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
string = input()
cnt = 0 # 크로아티아 알파벳 개수
for i in data:
    cnt += string.count(i)
print(len(string) - cnt)



# 구현
# replace 활용