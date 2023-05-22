from collections import Counter

T = int(input())
for _ in range(T):
    n = int(input())
    d = list(map(int, input().split()))
    dc = Counter(d)

    total = 0
    a = []
    m = max(dc)
    for i in d:
        if i != m:
            total += m-i

        if dc[i] == 1:
            dc.pop(i)
            if i == m and dc:
                m = max(dc)
        else:
            dc[i] -= 1
    print(total)