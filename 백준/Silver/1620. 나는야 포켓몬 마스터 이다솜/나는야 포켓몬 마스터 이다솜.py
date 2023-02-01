import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = {}
for i in range(1, n+1):
    data[input().rstrip()] = i
    
data2 = dict((v, k) for k, v in data.items())

for _ in range(m):
    wnt = input().rstrip()
    if wnt.isdigit():
        print(data2[int(wnt)])
    elif wnt.isalpha():
        print(data[wnt])