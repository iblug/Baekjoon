import heapq

def get_stamina(pick, mineral):
    if pick == 0:
        r = sum(mineral)
    elif pick == 1:
        r = mineral[0]*5 + mineral[1] + mineral[2]
    else:
        r = mineral[0]*25 + mineral[1]*5 + mineral[2]
    return -r


def solution(picks, minerals):
    answer = 0
    g = sum(picks)
    t = min(len(minerals), g*5)
    r = []
    z = []
    for i in range(0, t, 5):
        now = minerals[i:i+5]
        a = [0]*3
        for j in now:
            if j == 'diamond':
                a[0] -= 1
            elif j == 'iron':
                a[1] -= 1
            else:
                a[2] -= 1
        heapq.heappush(r, a)

    while r:
        b = heapq.heappop(r)
        if picks[0]:
            answer += get_stamina(0, b)
            picks[0] -= 1
        elif picks[1]:
            answer += get_stamina(1, b)
            picks[1] -= 1
        elif picks[2]:
            answer += get_stamina(2, b)
            picks[2] -= 1

    return answer