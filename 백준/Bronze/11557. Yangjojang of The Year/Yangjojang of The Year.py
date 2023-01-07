t = int(input())
for i in range(t):
    n = int(input())
    top_l = 0
    for j in range(n):
        s , l = input().split()
        l = int(l)
        if l > top_l:
            top_l = l
            top = s
    print(top)
