import heapq

# food_times = [3, 1, 2]
# k = 5

food_times = [8, 6, 4]
k = 15

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    time = 0
    nam = len(food_times)
    pre = 0

    q = []
    for i in range(nam):
        heapq.heappush(q, (food_times[i], i + 1))

    while time + ((q[0][0] - pre) * nam) <= k:
        now = heapq.heappop(q)[0]
        time += (now - pre) * nam
        nam -= 1
        pre = now

    result = sorted(q, key =lambda x:x[1])
    return result[(k - time) % nam][1]

print(solution(food_times, k))