# https://www.acmicpc.net/problem/2675
# 문자열 반복

import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

for _ in range(T):
    result = ''
    r, s = input().split()

    for i in s:
        for _ in range(int(r)):
            result += i
    print(result)