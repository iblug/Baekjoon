a, b = map(int, input().split())
nums = []
for i in range(1, 50):
    for _ in range(i):
        nums.append(i)
r = 0
for j in range(a-1, b):
    r += nums[j]
print(r)