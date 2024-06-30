y, m, d = map(int, input().split('-'))
if m == 9 and d > 16:
    print("TOO LATE")
elif m >= 10:
    print("TOO LATE")
else:
    print("GOOD")