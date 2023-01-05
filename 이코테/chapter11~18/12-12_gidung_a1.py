n = 5
build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1],
               [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
# build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1],
#                [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0],
#                [1, 1, 1, 0], [2, 2, 0, 1]]
def possible(answer):
    for i in answer:
        x, y, stuff = i
        if stuff == 0:
            if y == 0 or [x, y - 1, 0] in answer or [x - 1, y, 1] in answer or [x, y, 1] in answer:
                continue
            return False
        if stuff == 1:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for i in build_frame:
        x, y, stuff, oper = i
        if oper == 0:
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
        if oper == 1:
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])
    return sorted(answer)

print(solution(n, build_frame))

# data=[[]] 추가해서 그려보기