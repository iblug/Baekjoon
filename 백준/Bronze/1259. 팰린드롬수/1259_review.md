# 1259. 팰린드롬수
## 제출한 답
* 숏코딩을 노렸지만 역시 더 짧게 코딩한 사람이 있었다
```py
while True:
    n=input()
    if n=='0':
        break
    print('yneos'[n!=n[::-1]::2])
```

## 풀이 과정
* for 문으로 일일이 확인
```py
while True:
    n = input()
    if n == '0':
        break
    for i in range(len(n)//2):
        if n[i] != n[-i-1]:
            print('no')
            break
    else:
        print('yes')
```

* 너무 긴거 같아서 슬라이싱 활용
```py
while True:
    n = input()
    if n == '0':
        break
    if n == n[::-1]:
        print('yes')
    else:
        print('no')
```

## 내가 생각하는 BEST 타인 답
```py
import sys
while 1:
    n = sys.stdin.readline()[:-1]
    if n == '0':
        break
    print("yes") if n == n[::-1] else print("no")
```
  * 반복문에서 input()을 할때는 sys.stdin 을 활용하자
  * 문자열을 받을 때는.strip()대신 [:-1] 가능 (글자수 8 vs 5, 속도는?)
  * while True: 대신 while 1:

## 숏코딩
```py
while int(s:=input()):print('yneos'[s!=s[::-1]::2])
```
  * `:=`활용해서 while에서 바로 0처리 하기
  * 한 줄 처리하기