T = int(input())

for t in range(1, T + 1):
    data = list(map(int, input().split()))
    print(f'#{t} {max(data)}')