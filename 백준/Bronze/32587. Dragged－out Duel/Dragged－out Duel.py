n = m = int(input())
a = input()
b = input()

w = 0
for i in range(n):
    if (a[i] == 'R' and b[i] == 'S') or (a[i] == 'S' and b[i] == 'P') or (a[i] == 'P' and b[i] == 'R'):
        w += 1
    elif a[i] == b[i]:
        m -= 1

print('victory') if w > m//2 else print('defeat')