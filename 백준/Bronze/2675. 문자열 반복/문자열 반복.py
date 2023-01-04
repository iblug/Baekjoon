t = int(input())

for _ in range(t):
    result = ''
    r, s = input().split()

    for i in s:
        for _ in range(int(r)):
            result += i
    print(result)