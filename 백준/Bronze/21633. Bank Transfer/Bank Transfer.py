t = int(input())
s = t*0.01+25
if s < 100:
    print(100.00)
elif s > 2000:
    print(2000.00)
else:
    print(f'{s:.2f}')