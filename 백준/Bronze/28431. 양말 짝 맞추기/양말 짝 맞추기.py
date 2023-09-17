d = set()
for _ in range(5):
    a = int(input())
    if a in d:
        d.remove(a)
    else:
        d.add(a)
print(*d)