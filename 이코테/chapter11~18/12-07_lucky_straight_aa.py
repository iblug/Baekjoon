import time

n = input()

start = time.time()

length = len(n) # 점수값의 총 자릿수
summary = 0

#
for i in range(length // 2):
    summary += int(n[i])

#
for i in range(length // 2, length):
    summary -= int(n[i])

#
if summary == 0:
    print("LUCKY")
else:
    print("READY")

end = time.time()

print(end - start)