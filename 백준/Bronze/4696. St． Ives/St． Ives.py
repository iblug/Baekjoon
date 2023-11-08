import sys
input = sys.stdin.readline

while (n := float(input())) :
    print(f'{round((1 + n + n**2 + n**3 + n**4), 2):.2f}')