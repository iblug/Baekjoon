import sys
input = sys.stdin.readline

def is_prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if not x%i:
            return False
    return True

t = int(input())
for _ in range(t):
    a = int(input())
    while True:
        if is_prime(a):
            print(a)
            break
        else:
            a += 1