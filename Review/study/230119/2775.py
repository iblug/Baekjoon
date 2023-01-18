# https://www.acmicpc.net/problem/2775
# 부녀회장이 될테야

graph = [[0] * 15 for _ in range(15)]
for i in range(15):
    graph[0][i] = i

for x in range(1, 15):
    for y in range(1, 15):
        for y1 in range(1, y+1):
            graph[x][y] += graph[x-1][y1]

# print(*graph[::-1], sep='\n')

T = int(input())

for _ in range(T):
    xx = int(input())
    yy = int(input())
    print(graph[xx][yy])

# 그림그려보기
# 무리하게 규칙찾지 말기
# 어렵게 생각하지 말기