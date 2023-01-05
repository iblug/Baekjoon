food_times = [3, 1, 2]
k = 5


def solution(food_times, k):
    answer = 0
    if sum(food_times) <= k:
        answer = -1
    else:
        while k:
            if food_times[answer] != 0:
                food_times[answer] -= 1
                k -= 1
            answer = (answer + 1) % len(food_times)
            if food_times[answer] == 0:
                answer = (answer + 1) % len(food_times)
        answer += 1

    return answer

print(solution(food_times, k))