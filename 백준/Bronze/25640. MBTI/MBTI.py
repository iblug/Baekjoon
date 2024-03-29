import sys
input = sys.stdin.readline

mbti = input().rsplit()
n = int(input())
r = 0
for _ in range(n):
    if mbti == input().split():
        r += 1
print(r)