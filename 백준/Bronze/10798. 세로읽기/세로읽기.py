data = []
for _ in range(5):
    lst = list(input())
    data.append(lst + ['']*(15-len(lst)))
for i in range(15):
    for j in range(5):
        print(data[j][i], end='')