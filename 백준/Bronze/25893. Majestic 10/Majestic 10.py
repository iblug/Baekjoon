import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a = list(map(int, input().split()))
    print(*a)
    a.sort()
    if a[0] >= 10:
        print("triple-double")
    elif a[1] >= 10:
        print("double-double")
    elif a[2] >= 10:
        print("double")
    else:
        print("zilch")
    print()