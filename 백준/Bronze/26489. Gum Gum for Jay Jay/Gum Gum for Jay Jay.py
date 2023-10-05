import sys
input = sys.stdin.readline

cnt = 0
while 1:
    if input().rstrip() != 'gum gum for jay jay':
        break
    cnt += 1
print(cnt)