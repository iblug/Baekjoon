import sys
input = sys.stdin.readline

s = input().rstrip()

print(len(s) + s.count('_')*5 + 2)