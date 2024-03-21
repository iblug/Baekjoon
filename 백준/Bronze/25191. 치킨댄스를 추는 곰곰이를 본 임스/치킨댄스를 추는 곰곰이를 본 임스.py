n = int(input())
a, b = map(int, input().split())
r = a//2 + b
print(r if n > r else n)