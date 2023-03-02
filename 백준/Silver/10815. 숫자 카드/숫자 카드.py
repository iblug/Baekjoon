import sys
input = sys.stdin.readline

data = {}
n = int(input())
s = list(map(int, input().split()))
for i in s:
    data[i] = 1
m = int(input())
t = list(map(int, input().split()))

for i in t:
    print(data.get(i,0), end=' ')