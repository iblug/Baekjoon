sum = 0
for _ in range(5):
    num = int(input())
    sum += num if num > 40 else 40
print(sum//5)