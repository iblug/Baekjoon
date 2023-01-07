n = int(input())

cnt = 0
while n > 2:
    if n == 4 or n == 7:
        cnt = -1
        break
    else:
        if n % 3 == 0:
            if n // 3 > 4:
                n -= 5
                cnt += 1
            else:
                n -= 3
                cnt += 1
        else:
            n -= 5
            cnt += 1
print(cnt)