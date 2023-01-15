# 2906 최대공약수와 최소공배수(GCD,LCM)
## 제출한 답
* 공책에서 규칙찾다가 의식의 흐름대로 코딩함
* **규칙, 공식 기억하기**
```py
a, b = sorted(map(int, input().split()))
a1, b1 = a, b
while True:
    if b % a == 0:
        print(a)
        break
    b, a = a, b % a

print(b1*a1//a)
```
* 코드 정리하자
  * sorted 필요 없음
  * a1, b1 필요 없음
  * while 탈출 더 깔끔하게
```py
a, b = map(int, input().split())
l = a * b
while a:
    b, a = a, b % a

print(b, l // b)
```
## 다른 사람
* 함수만들기
  * 써볼까 하다가 그냥 위 방법대로 풀었음
```py
def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
a, b = map(int, input().split())
print(gcd(a, b))
print(a*b // gcd(a, b))
```
* 나머지는 비슷함

## 숏코딩
```py
a,b=map(int,input().split());L=a*b
while b:a,b=b,a%b
print(a,L//a)
```