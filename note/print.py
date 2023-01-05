# #유니코드(32~126)로 출력..(형변환 출력)(유니코드..)
# f = 32
# print(bin(f), oct(f), hex(f))
# # 0b11111 0o37 0x1f
# print(ord('D')) # 68
# print(chr(70)) # F


# # join 활용 리스트 출력
# str = 'hello'
# print(' '.join(str))
# arr = ['1', '2', '3'] # 문자열만 가능
# print(' '.join(arr))



# 인덱싱 슬라이스 스텝 출력
# a = [1, 2, 3, 4, 5]
# print(a[2::1])
#
# 인덱스 출력 # 성적, 농도 범위 출력
# print('FFFFFFDCBAA'[int(input())//10])
#
# 조건 출력
# a,b=map(int,input().split())
# print(['><'[a<b],'=='][a==b])
#
# 조건출력
# dust = int(input())
# print(((('좋음','보통')[dust > 30], '나쁨')[dust > 80],'매우 나쁨')[dust > 150])
#


# # 2차원 리스트 출력
# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for row in arr: # 첫번째 방법
#     print(row)
# print(*arr, sep='\n') # 두번째 방법




# 문자열에 변수넣기(Search Google... python variable string)
# .포맷..
#
# name = '광배'
# age = 30.1
# print(name + '는 ' + str(age) + '살입니다.')
# print('{}는 {}살입니다.'.format(name, age))
# print(f'{name}는 {age}살입니다.)
#
# name = 'Kim'
# score = 4.50001
# print(f'Hello, {name}! 성적은 {score:3.3f}')
#
# print(round(a, 2)) # 1234.57 # float
# print(round(a, 0)) # 1235.0
# print(round(a)) # 1235 # int
# print(round(a, -2)) # 1200.0



