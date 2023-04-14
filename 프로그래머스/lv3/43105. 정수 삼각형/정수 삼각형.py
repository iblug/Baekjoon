def solution(triangle):
    N = len(triangle)
    new = []
    left = right = 0
    for i in range(N):
        new.append([])
        for j in range(i+1):
            if j == 0:
                left = 0
            else:
                left = new[i-1][j-1]
            if j == i:
                right = 0
            else:
                right = new[i-1][j]
            new[i].append(triangle[i][j] + max(left, right))
    answer = max(new[i])
    return answer