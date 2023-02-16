def bur(n, x):
    if n == 0:
        if x == 0:
            return 0
        else:
            return 1
    bb = 2**(n+1)-3 # 이전 단계 버거크기
    pp = 2**n-1     # 이전 단계 패티 개수
    b = 2**(n+2)-3
    p = 2**(n+1)-1  # 현재 단계 패티 개수
    
    # 분할
    if x == 1:  # 왼쪽 끝
        return 0
    elif bb+2 > x:  # 왼쪽
        return bur(n-1, x-1)
    elif bb+2 == x: # 중앙
        return pp + 1
    elif bb+2 < x < b:  # 오른쪽
        return pp + 1 + bur(n-1, x-bb-2)
    else: #  끝
        return p

N, X = map(int, input().split())
print(bur(N, X))