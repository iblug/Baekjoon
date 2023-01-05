# N을 입력받기
n = int(input())

import time
stime = time.time()

count = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

etime = time.time()

print(count)
print(etime-stime)