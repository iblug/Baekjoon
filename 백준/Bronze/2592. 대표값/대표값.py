d = {}
sum_ = 0
for _ in range(10):
    num = int(input())
    sum_ += num
    d[num] = d.get(num, 0) + 1

print(sum_//10)
d = sorted(d.items(), key=lambda x: x[1])
print(d[-1][0])