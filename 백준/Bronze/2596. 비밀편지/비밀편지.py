P = ['000000', '001111', '010011', '011100', '100110', '101001', '110101', '111010']
n = int(input())
s = input()
r = ''
for i in range(0, n*6, 6):
    a = s[i:i+6]
    for j in range(8):
        cnt = 0
        for k in range(6):
            if a[k] == P[j][k]:
                cnt += 1
        if cnt >= 5:
            r += chr(65+j)
            break
    else:
        r = i//6 + 1
        break
print(r)