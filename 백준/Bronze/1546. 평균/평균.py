n = int(input())
score = list(map(int, input().split()))
r = 0

for i in score:
    r += i / max(score) * 100
print(r/len(score))