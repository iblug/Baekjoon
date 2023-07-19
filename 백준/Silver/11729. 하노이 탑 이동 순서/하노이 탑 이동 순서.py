import sys
print = sys.stdout.write

def h(n, start, mid, end):
    if n == 1:
        print(f'{start} {end}\n')
        return
    
    h(n-1, start, end, mid)
    print(f'{start} {end}\n')
    h(n-1, mid, start, end)

n = int(input())
print(f'{2**n-1}\n')
h(n, 1, 2, 3)