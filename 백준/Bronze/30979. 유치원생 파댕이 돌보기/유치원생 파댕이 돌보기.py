import sys
input = sys.stdin.readline

t = int(input())
input()
s = sum(map(int, input().split()))
print("Padaeng_i Cry" if t > s else "Padaeng_i Happy")