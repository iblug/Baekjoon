n = int(input())
for _ in range(n):
    a = input()
    b = input()
    c = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            c += 1
    print(f"Hamming distance is {c}.")