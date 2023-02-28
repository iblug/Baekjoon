import sys
input = sys.stdin.readline

while 1:
    r1 = [1]
    r2 = []
    s = 1
    n = int(input())
    if n == -1:
        break
    for i in range(2, int(n**0.5)+1):
        if not n % i:
            if i**2 == n:
                s += i
                r1.append(i)
            else:
                s += i + n//i
                r1.append(i)
                r2.append(n//i)
            if s > n:
                print(n, 'is NOT perfect.')
                break
    else:
        # print(r1, r2, s)
        if s == n:
            print(n, '=',' + '.join(map(str, r1)), '+', ' + '.join(map(str, r2[::-1])))
        else:
            print(n, 'is NOT perfect.')