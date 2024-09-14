import sys
input = sys.stdin.readline

n = int(input())
while m := int(input()):
    if m % n:
        print(f'{m} is NOT a multiple of {n}.')
    else:
        print(f'{m} is a multiple of {n}.')