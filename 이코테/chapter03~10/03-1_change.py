# 거스름돈

n = 1260
count = 0

# 큰 단위의 화폐부터 자례대로 확인
c_list: list[int] = [500, 100, 50, 10]

for coin in c_list:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)