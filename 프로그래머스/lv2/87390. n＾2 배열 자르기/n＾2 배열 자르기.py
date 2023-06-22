def solution(n, left, right):
    answer = []
    a = left//n
    aa = left%n
    b = right//n
    bb = right%n
    if a == b:
        answer = [i+1 if i > a else a+1 for i in range(n)][aa:bb+1]
    else:
        answer += [i+1 if i > a else a+1 for i in range(n)][aa:]
        for k in range(a+1, b):
            answer += [i+1 if i > k else k+1 for i in range(n)]
        answer += [i+1 if i > b else b+1 for i in range(n)][:bb+1]
    return answer