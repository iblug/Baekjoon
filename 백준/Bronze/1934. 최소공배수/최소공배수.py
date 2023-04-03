def f(a, b):
    if a == 0:
        return b
    return f(b%a, a)

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(int(a*b / f(a, b)))
