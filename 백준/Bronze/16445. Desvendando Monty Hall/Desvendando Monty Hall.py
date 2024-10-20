import sys
input = sys.stdin.readline

n = int(input())
l = [input().rstrip() for _ in range(n)]
print(n - l.count('1'))