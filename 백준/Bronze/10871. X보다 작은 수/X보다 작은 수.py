n, x = map(int, input().split())
a = list(map(int, input().split()))

print(*(list(i for i in a if i < x)))