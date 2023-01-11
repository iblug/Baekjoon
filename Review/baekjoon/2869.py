# https://www.acmicpc.net/problem/2869
# 달팽이는 올라가고 싶다

import math
a, b, v = map(int, input().split())
print(math.ceil((v-a) / (a-b)) + 1)

# 다른풀이

# (v-b-1) / (a-b)) + 1 # 소수점 처리 필요 없다?!
# (v-b) / (a-b)