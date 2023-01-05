# https://school.programmers.co.kr/learn/courses/30/lessons/42891

food_times = [3, 1, 2]
k = 5


def solution(food_times, k):
    answer = 0
    if sum(food_times) <= k:
        answer = -1
    else:
        while k:
            for i in range(len(food_times)):
                if food_times[i] != 0:
                    food_times[i] -= 1
                    k -= 1
                    if i == len(food_times):
                        answer = 1
                    else:
                        answer = i
    return answer

result = solution(food_times, k)

print(result)