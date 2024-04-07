import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a = list(map(int, input().split()))
    print(*a)
    if 17 in a and 18 in a:
        print("both")
    elif 17 in a:
        print("zack")
    elif 18 in a:
        print("mack")
    else:
        print("none")
    print()