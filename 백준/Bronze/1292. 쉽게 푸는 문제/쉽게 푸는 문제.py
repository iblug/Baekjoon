a, b = map(int, input().split())
nums = []
k=0
for i in range(1, b+1):
    k+=1
    for _ in range(i):
        nums.append(k)
print(sum(nums[a-1:b]))