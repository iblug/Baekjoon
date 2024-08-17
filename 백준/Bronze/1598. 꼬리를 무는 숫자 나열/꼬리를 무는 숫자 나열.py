n, m = map(int, input().split())

x1 = n//4 if n%4 else (n//4) - 1
y1 = n % 4 if n%4 else 4
x2 = m//4 if m%4 else (m//4) - 1
y2 = m % 4 if m%4 else 4

print(abs(x2 - x1) + abs(y2 - y1))