import sys
input = sys.stdin.readline

while True:
    a, *l = map(int, input().split())
    if a == 0:
        break
    r = 1
    for i in range(0, 2*a, 2):
        r = r * l[i] - l[i+1]
    print(r)