def solution(p:list):
    answer = [0]*len(p)
    stack = []

    for i, price in enumerate(p):
        while stack and price < p[stack[-1]]:
            t = stack.pop()
            answer[t] = i-t
        stack.append(i)
    while stack:
        t = stack.pop()
        answer[t] = len(p)-1-t
    
    return answer