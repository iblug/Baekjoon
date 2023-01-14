# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QSEhaA5sDFAUq
T = int(input())

for t in range(1, T + 1):
    data = list(map(int, input().split()))
    result = [num for num in data if num % 2]
    
    print(f'#{t} {sum(result)}')

# 백준Hub 연동이 안된다