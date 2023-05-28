import sys
input = sys.stdin.readline

e = [int(input()) for _ in range(5)]
print(min(e[:3])+min(e[3:])-50)