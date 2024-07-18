input()
f = True
for _ in range(3):
    s = input()
    if '7' not in s:
        f = False
        break
print('777' if f else '0')