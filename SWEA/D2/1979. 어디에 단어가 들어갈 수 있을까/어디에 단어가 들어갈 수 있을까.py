T = int(input())

for t in range(T):
    n, k = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(n)]
    key = [1]*k

    cnt = 0
    for i in d:
        for j in range(0,n-k):
            if j == 0:
                if i[:k+1] == key + [0]:
                    cnt += 1
            if j == n-k-1:
                if i[n-k-1:] == [0] + key:
                    cnt += 1
            if i[j:j+k+2] == [0] + key + [0]:
                cnt += 1
        if n == k:
            if i == key:
                cnt += 1
    d = list(map(list, zip(*d)))
    for i in d:
        for j in range(0,n-k):
            if j == 0:
                if i[:k+1] == key + [0]:
                    cnt += 1
            if j == n-k-1:
                if i[n-k-1:] == [0] + key:
                    cnt += 1
            if i[j:j+k+2] == [0] + key + [0]:
                cnt += 1
        if n == k:
            if i == key:
                cnt += 1
    print(f'#{t+1} {cnt}')