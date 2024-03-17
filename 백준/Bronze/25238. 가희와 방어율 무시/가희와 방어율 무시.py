a, b = map(int, input().split())
print('01'[a*((100-b)/100) < 100])