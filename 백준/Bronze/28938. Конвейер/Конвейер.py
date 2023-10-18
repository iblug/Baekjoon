input()
n = sum(map(int, input().split()))
if n > 0:
    print('Right')
elif n < 0:
    print('Left')
else:
    print('Stay')