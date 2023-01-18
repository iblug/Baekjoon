# https://www.acmicpc.net/problem/10886
# 0 = not cute / 1 = cute

import sys
# import time
sys.stdin = open('input.txt', 'r')


n = int(input())
# start = time.time()
'''
s = ''
for _ in range(n):
    s += input()
    # s += sys.stdin.readline().rstrip()
# print(s)
# print(s.count('0'))
if s.count('0') > n // 2:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')

'''
# 리스트를 쓰거나 변수 들어올때마다 cnt하자

cnt = 0
for _ in range(n):
    if input() == '0':
        cnt = 1
if cnt > n // 2:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')


# end = time.time()
# print(end - start)


# 더 간단하게
cnt = 0
for _ in range(n):
    cnt += int(input())

if cnt > n // 2:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')


########################### 다른 사람
N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))

#if max(nums, key=lambda x: nums.count(x)) == 1:
if max(nums, key=nums.count) == 1:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")

# 방법이 다양한거 같다

# * sum = 0 해서 더한 다음 is > n//2 ?

# * 리스트에 따로

