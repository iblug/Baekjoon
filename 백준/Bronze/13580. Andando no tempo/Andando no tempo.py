a = sorted(map(int, input().split()))
if sum(a)/2 in a or len(set(a)) < 3:
    print("S")
else:
    print("N")