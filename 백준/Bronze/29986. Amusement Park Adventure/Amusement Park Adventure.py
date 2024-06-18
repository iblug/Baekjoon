n, h = map(int, input().split())
a = map(int, input().split())

print(sum(map(lambda x : x <= h, a)))