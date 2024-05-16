import sys, math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a1, p1 = map(int, input().split())
    r1, p2 = map(int, input().split())

    print('Whole pizza' if a1/p1 < r1**2*math.pi/p2 else 'Slice of pizza')