# https://school.programmers.co.kr/learn/courses/30/lessons/60059

lock = [[1,1,1],[1,1,0],[1,0,1]]
key = [[0,0,0],[1,0,0],[0,1,1]]
n = len(lock)
m = len(key)

def tr(x):
    m = len(x)
    t = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            t[i][j] = x[m-j-1][i]
    return t

def solution(key, lock):
    answer = 0
    return answer
