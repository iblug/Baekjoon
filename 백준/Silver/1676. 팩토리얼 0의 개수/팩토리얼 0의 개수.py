def fact(x):
    if x == 0 or x == 1:
        return 1
    return x * fact(x-1)

n = int(input())

cnt = 0
m = str(fact(n))
for i in range(1, len(m)):
    if m[-i] == '0':
        cnt += 1
    else:
        break
print(cnt)