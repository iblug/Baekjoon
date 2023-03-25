T = int(input())
d = ['a', 'e', 'i', 'o', 'u']
for t in range(T):
    s = input()
    for i in d:
        s = s.replace(i,'')
    print(f'#{t+1} {s}')