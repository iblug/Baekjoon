import sys
input = sys.stdin.readline
c = input().rstrip()
if c == '고무오리 디버깅 시작':
    stack = []
    while True:
        c = input().rstrip()
        if c == '문제':
            stack.append('문제')
        elif c == '고무오리':
            if stack:
                stack.pop()
            else:
                stack.append('문제')
                stack.append('문제')
        elif c == '고무오리 디버깅 끝':
            break
    if stack:
        print('힝구')
    else:
        print('고무오리야 사랑해')