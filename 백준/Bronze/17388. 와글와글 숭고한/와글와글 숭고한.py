a, b, c = map(int, input().split())
if a + b + c >= 100:
    print("OK")
else:
    m = min(a, b, c)
    if m == a:
        print("Soongsil")
    elif m == b:
        print("Korea")
    else:
        print("Hanyang")