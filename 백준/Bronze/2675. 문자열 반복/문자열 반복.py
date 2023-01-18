T = int(input())

for _ in range(T):
    a, b = input().split()
    for i in b:
        print(i*int(a), end='')
    print()