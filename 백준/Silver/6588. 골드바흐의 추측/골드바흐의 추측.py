import sys
input = sys.stdin.readline

SIZE = 1000000

prime = [True] * (SIZE + 1)
prime[0] = False
prime[1] = False

for i in range(2, (SIZE + 1) // 2):
    if not prime[i]:
        continue
    for j in range(i * 2, SIZE, i):
        prime[j] = False
primes = [i for i in range(SIZE) if prime[i]]

while True:
    n = int(input())
    if not n:
        break
    for i in primes:
        if prime[i] and prime[n-i]:
            print(f'{n} = {i} + {n-i}')
            break