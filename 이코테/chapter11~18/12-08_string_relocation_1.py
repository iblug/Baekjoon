x = ['0', '9', 'A', 'Z', 'a', 'z']
print(x)
for i in range(len(x)):
    print(ord(x[i]), end=' ')
print('\n')

# s = list(input().split(sep=''))
# s=['k', '1', 'k', 'a', '5', 'c', 'b', '7']

s = input()
c = []
n = []

for i in s:
    if ord(i) in range(48, 58):
        n.append(int(i))
    else:
        c.append(i)
c.sort()
for i in c:
    print(i,end='')
print(sum(n))

'''
K1KA5CB7
AJKDLSI412K4JSJ9D
'''
