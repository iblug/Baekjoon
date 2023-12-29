import sys
input = sys.stdin.readline

a = [input().rstrip() for _ in range(6)]
print([1, 2, 3, -1][a.count('L')//2])
