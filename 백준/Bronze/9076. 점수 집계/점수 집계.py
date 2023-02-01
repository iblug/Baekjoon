t = int(input())
for _ in range(t):
    scores = list(map(int, input().split()))
    scores = sorted(scores)
    if scores[-2] - scores[1] >= 4:
        print('KIN')
    else:
        print(sum(scores[1:-1]))