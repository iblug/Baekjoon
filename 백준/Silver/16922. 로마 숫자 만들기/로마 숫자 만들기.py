n = int(input())

r = set()
for i in range(n+1):
    for j in range(n+1):
        for k in range(n+1):
            for l in range(n+1):
                if i + j + k + l == n:
                    r.add(i+j*5+k*10+l*50)

print(len(r))