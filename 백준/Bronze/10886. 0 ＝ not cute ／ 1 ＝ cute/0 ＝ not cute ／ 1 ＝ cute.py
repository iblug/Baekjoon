n = int(input())
s = ''
for _ in range(n):
    s += input()

if s.count('0') > len(s)//2:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')