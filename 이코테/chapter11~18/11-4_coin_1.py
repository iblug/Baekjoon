n = int(input())
coin = list(map(int, input().split()))
graph = [] * int(2e9)

coin.sort(reverse=True)


for i in range(1, int(2e9)):
    for j in coin:
        c = i
        if c - j != 0:
            c -= j
        else:

print(coin)