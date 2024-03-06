import sys
input = sys.stdin.readline

s = 0
while True:
    n = int(input())
    if n > 0:
        s += n
    else:
        break
print(s)