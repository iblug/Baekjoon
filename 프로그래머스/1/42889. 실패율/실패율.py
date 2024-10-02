def solution(N, stages):
    person = len(stages)
    p = [0] * (N +2)
    for i in stages:
        p[i] += 1
    r = []
    for i in range(N+1):
        if person > 0:
            r.append((p[i]/person,i))
        else:
            r.append((0,i))
        person -= p[i]
    r = sorted(r[1:], key=lambda x: (-x[0],x[1]))
    answer = [y for x,y in r]
    return answer