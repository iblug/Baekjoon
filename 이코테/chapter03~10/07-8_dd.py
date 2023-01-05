# 떡의 개수(N)와 요청한 떡의 길이(M)을 입렵받기
n, m = map(int, input().split(' '))
# 각 떡의 개별 높이 정보를 입력받기
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

''' 내가 짠 코드
while start <= end:
    result = 0
    mid = (start + end) // 2
    for i in array:
        if i < mid:
            continue
        result += i - mid
    if result == m:
        print(mid)
        break
    elif result > m:
        start = mid + 1
    else:
        end = mid -1
'''

# 이진 탐색 수행(반복적)
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for i in array:
        # 잘랐을 때이 떡의 양 계산
        if i > mid:
            total += i - mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탑색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1

# 정답 출력
print(result)