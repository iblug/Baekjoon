n = int(input())
r = list(map(int, input().split()))
sum = 0
s = 0
for i in r:
    if i == 1:
        s +=1
        sum += s
    else:
        s = 0
print(sum)