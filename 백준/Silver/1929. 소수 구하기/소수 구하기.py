m, n = map(int, input().split())

data = [1]*(n+1)
data[1] = 0
for i in range(2, int(n**0.5)+1):
    if data[i] == 1:
        for j in range(2*i, n+1, i): 
            data[j] = 0
for k in range(m, n+1):
    if data[k] == 1:
        print(k)