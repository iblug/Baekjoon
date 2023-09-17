def f(a, b): 
    if a == 0:
        return b
    return f(b%a, a)

d = input()
j = int(d[2:])
m = 10**(len(d)-2)
c = f(j, m)
print('YES')
print(int(j/c), int(m/c))