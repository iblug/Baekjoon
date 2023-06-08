in_data = 'baby sukhwan tururu turu very cute tururu turu in bed tururu turu baby sukhwan'
data = list(in_data.split())
N = int(input())
n = (N-1)%14
m = (N-1)//len(data)
if data[n] == 'tururu':
    if m < 3:
        print('tururu'+'ru'*m)
    else:
        print(f'tu+ru*{m+2}')
elif data[n] == 'turu':
    if m < 4:
        print('turu'+'ru'*m)
    else:
        print(f'tu+ru*{m+1}')
else:
    print(data[n])