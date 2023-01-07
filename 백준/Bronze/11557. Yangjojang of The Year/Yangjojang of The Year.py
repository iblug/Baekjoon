t = int(input())
for i in range(t):
    n = int(input())
    top = ''
    top_l = 0
    for j in range(n):
        s , l = input().split()
        l = int(l)
        top_l = max(l, top_l)
        if l == top_l:
            top = s
    print(top)
