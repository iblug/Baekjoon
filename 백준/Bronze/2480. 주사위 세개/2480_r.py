# https://www.acmicpc.net/problem/2480
# 주사위 세개

import sys
sys.stdin = open('input.txt', 'r')

a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a * 1000)
elif (a == b) or (a == c): # b != c
    print(1000 + a * 100)
elif b == c: # a != b
    print(1000 + b * 100)
else: # a != b != c
    print(max(a, b, c) * 100)


#######################다른사람

# 리스트에 주사위 숫자 나온 횟수 저장

lst_count = [0 for _ in range(6)]
lst_input = list(map(int, input().split()))
for i_1 in lst_input:
    lst_count[i_1 - 1] += 1
if max(lst_count) == 3:
    print(10000 + 1000 * (lst_count.index(3) + 1))
elif max(lst_count) == 2:
    print(1000 + 100 * (lst_count.index(2) + 1))
else:
    print(100 * max(lst_input))

# Set 이용
dice = list(map(int, input().split()))
set_dice = set(dice)

if len(set_dice) == 1:
    price = 10000 + set_dice.pop() * 1000

elif len(set_dice) == 3:
    dice.sort()
    price = dice.pop() * 100

else:
    dice.sort()
    
    if dice[0] == dice[1]:
        price = 1000 + dice[0] * 100

    else:
        price = 1000 + dice[1] * 100

print(price)

## count 하기

Dices = list(map(int, input().split()))
for Dice in Dices:
    if 3 == Dices.count(Dice):
        print(10000 + (Dice * 1000))
        break
    elif 2 == Dices.count(Dice):
        print(1000 + (Dice * 100))
        break
    else:
        print(max(Dices)*100)
        break