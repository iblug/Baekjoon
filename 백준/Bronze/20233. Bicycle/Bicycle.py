import sys
input = sys.stdin.readline

a = int(input())
x = int(input())
b = int(input())
y = int(input())
t = int(input())

print(((t-30) * x * 21 + a) if t > 30 else a, ((t-45) * y * 21 + b) if t > 45 else b)