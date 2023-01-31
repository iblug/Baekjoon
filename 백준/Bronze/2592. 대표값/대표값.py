from collections import Counter
d = [int(input()) for _ in range(10)]
c = Counter(d)

print(sum(d)//10)
print(c.most_common(1)[0][0])