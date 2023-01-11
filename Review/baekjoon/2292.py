# https://www.acmicpc.net/source/53768402
# 벌집

data = int(input())
i = 1

while True:
    if data <= i * (i - 1) * 3 + 1:
        break
    i += 1

print(i)

# 규칙을 찾았는데 삽질하느라 시간을 많이 썼다 ㅠ