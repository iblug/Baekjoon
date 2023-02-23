n, m = map(int, input().split())
s = input()
if s.count('A') < 2:
    print('NO')
    exit()
k = n-m

result = ''
i = 1
while True:
    if s[-i] not in ['A', 'E', 'I', 'O', 'U']:
        result += s[-i]
        i += 1
        break
    i += 1
    k -= 1
    if i > n or k < 0:
        break
if not result:
    print('NO')
    exit()

cnt = 0
while True:
    if s[-i] == 'A':
        cnt += 1
        result += s[-i]
    else:        
        k -= 1
    i += 1
    if i > n or k < 0 or cnt == 2:
        break
ss = s[:-i+1] 
if len(result) < 3:
    print('NO')
    exit()
if k < 0:
    print('NO')
    exit()
kk = len(ss)-(m-3)

ans = ss[kk:]+''.join(result[::-1])

print(ans)