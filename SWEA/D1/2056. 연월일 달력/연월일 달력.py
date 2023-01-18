# 제출한 답

T=int(input())
data=[-1,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for t in range(1, T + 1):
    ymd=input()
    y=ymd[:4]
    m=ymd[4:6]
    d=ymd[6:]
    if int(m)>12 or int(d)>data[int(m)]: 
        result=-1
    else:
        result=f'{y}/{m}/{d}'
    print(f'#{t} {result}')

# 0월일때 -1 쓰지말고 인덱스에서 int(m)-1 방법도 있긴 한데..

# m > 12일때 if문 data[int(m)]에서 인덱스 에러가 발생하지 않는다! 
# 파이썬만 이런가? 갓이썬..킹이썬..
""" 
if int(m) > 12:
    result = -1
elif int(d) > data[int(m)]:
    result = -1
"""

# 다양한 풀이가 있는 것 같다

# 윤년일때..로 응용 가능할 것 같다