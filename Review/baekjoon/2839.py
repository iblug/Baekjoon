# https://www.acmicpc.net/problem/2839
# 설탕 배달

n = int(input())

cnt = 0
while n > 2:
    if n == 4 or n == 7:
        cnt = -1
        break
    elif n % 5 == 0:
        cnt += n // 5
        break
    else:
        if n % 3 == 0:
            if n // 3 > 4:
                n -= 5
                cnt += 1
            else:
                n -= 3
                cnt += 1
        else:
            n -= 5
            cnt += 1
print(cnt)


# elif 블럭은 없어도 정답
# 구현하기 위해 시간 너무 많이 썼다 그래도 해결했다!
# 그리디 알고리즘?
# 더 좋고 깔끔한 해결은 없나?

#################################################

# 깔끔한 방법
# while-else