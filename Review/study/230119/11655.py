# https://www.acmicpc.net/problem/11655
# 11655 ROT13

S = input()
result = ''
for i in S:
    if i.islower(): # -97 + 13 = -84
        result += chr((ord(i)-84)%26+97)
    elif i.isupper(): # -65 + 13 = -52
        result += chr((ord(i)-52)%26+65)
    else:
        result += i
print(result)







# 알파벳아닌 문자 처리하기
# 원본 S를 바꾸려면?




## 
""" 
S = input().split()

result = []
for i in range(len(S)):
    r=''
    for j in S[i]:
        if j.islower(): # -97 + 13 = -84
            r += chr((ord(j)-84)%26+97)
            # S[i] = S[i].replace(j, chr((ord(j)-84)%26+97))
        elif j.isupper(): # -65 + 13 = -52
            r += chr((ord(j)-52)%26+65)
            # S[i] = S[i].replace(j, chr((ord(j)-52)%26+65))
        elif j.isnumeric:
            r += j
    result.append(r)
# print(' '.join(S))
# print(result)
print(' '.join(result))
# print(' '.join(result), 'abc')
# print(type(' '.join(result)))
"""