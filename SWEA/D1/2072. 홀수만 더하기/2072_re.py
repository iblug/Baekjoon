T = int(input())

for t in range(1, T + 1):
    # data = 
    result = [num for num in list(map(int, input().split())) if num % 2]
    
    print(f'#{t} {sum(result)}')

# 백준허브 연동 안됨