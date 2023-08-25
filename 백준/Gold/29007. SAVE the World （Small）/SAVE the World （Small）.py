N = 30

def go(b, c):
    if b < 0 and c < 0: # 3
        return 0
    elif b < 0 and c == 0:
        return 1
    elif b < 0 and c > 0: # 2
        return 2
    elif b == 0 and c > 0:
        return 3
    elif b > 0 and c > 0: # 1
        return 4
    elif b > 0 and c == 0:
        return 5
    elif b > 0 and c < 0: # 4
        return 6
    elif b == 0 and c < 0:
        return 7

dxy = [(1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)]
bot = ['E', 'D', 'C', 'X', 'Z', 'A', 'Q', 'W']

def dfs(x, y, cnt):
    s = [(x, y, cnt)]
    v = [[0]*(N+1) for _ in range(N+1)]
    v[y][x] = cnt
    while s:
        x, y, cnt = s.pop()
        board[y][x].add(cnt)
        if x == 0 == y:
            return
        # 방향 우선 처리
        start = go(x, y)
        for i in range(start, start+8):
            i %= 8
            nx = x + dxy[i][0]
            ny = y + dxy[i][1]
            if nx >= N//2 or nx < -(N//2) or ny >= N//2 or ny < -(N//2):
                continue
            if v[ny][nx]:
                if i == (start+7)%8:
                    v = [[0]*(N+1) for _ in range(N+1)]
                    s.append((x, y, cnt))
                continue
            if (cnt + 1) in board[ny][nx]:
                continue
            s.append((nx, ny, cnt+1))
            v[ny][nx] = cnt
            print(bot[i], end='')
            break

n = int(input())
board = [[set() for _ in range(N+1)] for _ in range(N+1)]
p = []
for _ in range(n):
    x, y = map(int, input().split())
    p.append((x, y))
for a, b in p:
    dfs(a, b, 1)
    print()