# https://school.programmers.co.kr/learn/courses/30/lessons/60061

n = 5
# build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1],
               # [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1],
               [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0],
               [1, 1, 1, 0], [2, 2, 0, 1]]

data = [[0] * (n + 1) for i in range(n + 1)]
datac = [[0] * (n + 1) for i in range(n + 1)]
datab = [[0] * (n + 1) for i in range(n + 1)]


# 미완성
def solution(n, build_frame):
    answer = [[]]
    for i in build_frame:
        x, y, a, b = i[0], i[1], i[2], i[3]
        if a == 0 and b == 0:  # 기둥 삭제
            if (y == 0 or datac[x][y] == 1) and datac[x][y + 1] == 1:
                datac[x][y], datac[x][y + 1] = 0
                continue
            else:
                continue
        if a == 0 and b == 1: # 기둥 설치
            if y == 0 or datab[x][y] or datac[x][y] == 1:
                datac[x][y], datac[x][y + 1] = 1
                continue
            else:
                continue
        if a == 1 and b == 0: # 보 삭제
            if datab[x][y] == 1 and datab[x + 1][y] == 1:
                datab[x + 1][y] = 0
                continue
            else:
                continue
        if a == 1 and b == 1:  # 보 설치
            if data[x][y] == 1 or data[x + 1][y] == 1:
                data[x + 1][y] = 1
                continue
            else:
                continue
    return answer

solution(n, build_frame)
print(data)