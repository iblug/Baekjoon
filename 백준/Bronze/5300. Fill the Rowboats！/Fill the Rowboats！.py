n = int(input())
for i in range(1, n+1, 6):
    for j in range(i, i+6):
        if j == n:
            print(j, end=' ')
            break
        print(j, end=' ')
    print('Go!', end=' ')
