Y = 'YONSEI'
K = 'KOREA'

i = j = 0
S = input()
for e in S:
    if Y[i] == e:
        i += 1
    if K[j] == e:
        j += 1
    if i == 6:
        print(Y)
        break
    if j == 5:
        print(K)
        break