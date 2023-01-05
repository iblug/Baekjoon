# N, K를 공백으로 구분하여 입력받기
n, k = map(int, input().split())

# 배열 A, B의 모든 원소를 입력받기
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 배열 A는 오른차순, 배열 B는 내림차순 정렬 수행
a.sort()
b.sort(reverse=True)

# 첫 번째 인덱스부터 확인하여, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    #
    if a[i] >= b[i]:
        break
    else:   #
        a[i], b[i] = b[i], a[i]

print(sum(a)) # 배열 A의 모든 원소의 합을 출력