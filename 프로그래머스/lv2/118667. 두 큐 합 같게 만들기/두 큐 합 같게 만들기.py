from collections import deque

def solution(q1:list, q2:list):
    l = len(q1)
    s1 = sum(q1)
    s2 = sum(q2)
    if (s1 + s2) % 2:
        return -1

    q1=deque(q1)
    q2=deque(q2)
    answer = 0
    while answer <= l*3:
        if s1 == s2:
            return answer
        if s1 > s2:
            temp = q1.popleft()
            q2.append(temp)
            s1 -= temp
            s2 += temp
        elif s1 < s2:
            temp = q2.popleft()
            q1.append(temp)
            s1 += temp
            s2 -= temp
        answer += 1
    return -1