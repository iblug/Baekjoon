w1, h1, w2, h2 = [int(input()) for _ in range(4)]
print(max(w1, w2) * 2 + (h1 + h2) *2 + 4)