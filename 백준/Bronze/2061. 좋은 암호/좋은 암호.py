p, k = map(int, input().split())
for i in range(2, k):
    if p % i:
        continue
    else:
        print('BAD', i)
        break
else:
    print('GOOD')