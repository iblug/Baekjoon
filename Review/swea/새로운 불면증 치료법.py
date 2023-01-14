def digits(N):
    result = set()
    while N > 0: 
        result.add(N % 10)
        N //= 10
    return result

T = int(input())

for t in range(1, T + 1):
    data = [0 for _ in range(10)]
    N = int(input())
    i = 0
    while True:
        i += 1
        n = N * i
        for num in digits(n):
            data[num] = 1
        if data.count(0):
            continue
        else:
            break
        
    print(f'#{t} {n}')

# 더 쉽게 풀자..