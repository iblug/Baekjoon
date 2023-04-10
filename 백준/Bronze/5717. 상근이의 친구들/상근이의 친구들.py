import sys
for i in sys.stdin:
    a = sum(map(int, i.split()))
    if a:
        print(a)