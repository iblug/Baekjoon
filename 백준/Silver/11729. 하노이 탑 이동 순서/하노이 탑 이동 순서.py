import sys
sys.setrecursionlimit(int(1e6))

def h(n, start, mid, end):
    if n == 1:
        print(start, end)
        return
    
    h(n-1, start, end, mid)
    print(start, end)
    h(n-1, mid, start, end)

n = int(input())
print(2**n-1)
h(n, 1, 2, 3)