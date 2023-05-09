W, H = map(int, input().split())
n = int(input())

def s():
    a, b = map(int, input().split())
    if a == 1:
        return b
    elif a == 2:
        return 2*W+H-b
    elif a == 3:
        return (H+W)*2-b
    else:
        return W+b

store = []
for _ in range(n):
    store.append(s())
d = s()
r = 0
for i in store:
    if abs(d-i) <= W+H:
        r += abs(d-i)
    else:
        r += (W+H)*2 - abs(d-i)
print(r)