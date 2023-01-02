c = int(input())

for _ in range(c):
    s = list(map(int, input().split()))
    l = len(s) - 1
    a = (sum(s) - s[0]) / l
    count = 0
    for i in s[1:]:
        if i > a:
            count += 1
    p = round(count / l * 100, 3)
    print(f'{p:.3f}%')