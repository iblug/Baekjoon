####################################################################
# 숏코딩

# # 윤년 숏코딩 분해
# y=list(map(int, input().split()))
# for i in range(len(y)):
#     print(+((y[i]%100 or y[i]//100)%4<1))
#     print(f'(1) {y[i]} % 100 =', y[i]%100)
#     print(f'(2) {y[i]} // 100 =', y[i]//100)
#     print(f'(3) (1) or (2) =', y[i]%100 or y[i]//100)
#     print(f'(4) (3) % 4 =', (y[i]%100 or y[i]//100)%4, '\n')

# # 숏코딩 사분면
# a,b=map(int,open(0))
# print('3421'[a>0::2][b>0]) 

# 1541 잃어버린 괄호 숏코딩 풀이
# https://bio-info.tistory.com/125#%EC%88%8F%EC%BD%94%EB%94%A91

# in : 0 4 2 5 6
# print(input()[::2])
# out : '04256'


# for i in open(0):
#     a, b, c = i.split()
#     print(a, b, c)
#
# print("wrriognhgt"[a*a+b*b==c*c:a*b:2]


# := 활용하기


########################################################


# https://www.acmicpc.net/problem/1000
# A+B
# > 1 2
# print(sum(map(int, input().split())))
# print(sum(b'2%a'%input())&31) # 유니코드?



# https://www.acmicpc.net/problem/2558
# > 1
# > 2

# num1 = int(input())
# num2 = int(input())
# print(num1 + num2)

# print(sum(map(int,open(0))))




# https://www.acmicpc.net/problem/10950
# > 5
# > 1 1
# > 2 3
# > 3 4
# > 9 8
# > 5 2

# T = int(input())
# for _ in range(T):
#     num1, num2 = map(int, input().split())
#     print(num1 + num2)

# for i in[*open(0)][1:]:print(sum(b'%a'%i)%24)




# https://www.acmicpc.net/problem/10953
# > 5
# > 1,1
# > 2,3
# > 3,4
# > 9,8
# > 5,2

# T = int(input())
# for _ in range(T):
#     num1, num2 = map(int, input().split(','))
#     print(num1 + num2)

# print(*map(sum,map(eval,[*open(0)][1:])))

# for s in[*open(0)][1:]:print(sum(eval(s)))





# https://www.acmicpc.net/problem/11021
# > 5
# > 1 1
# > 2 3
# > 3 4
# > 9 8
# > 5 2

# T = int(input())
# for t in range(1, T + 1):
#     num1, num2 = map(int, input().split())
#     print(f'Case #{t}: {num1 + num2}')

# i=1
# for s in[*open(0)][1:]:print(f'Case #{i}:',sum(b'%a'%s)%34);i+=1

# i=0
# for a,_,c,_ in[*open(0)][1:]:i+=1;print(f'Case #{i}:',int(a)+int(c))




# https://www.acmicpc.net/problem/11022
# > 5
# > 1 1
# > 2 3
# > 3 4
# > 9 8
# > 5 2

# T = int(input())
# for t in range(1, T + 1):
#     num1, num2 = map(int, input().split())
#     print(f'Case #{t}: {num1} + {num2} = {num1 + num2}')

# i=0
# for a,_,c,_ in[*open(0)][1:]:i+=1;print(f'Case #{i}:',a,'+',c,'=',int(a)+int(c))

##############################################################################################

# *b이후의 값을 list로 b에 저장
# 숏코딩때 유용
# a,*b=map(int,sys.stdin.readline().split()) # *b

