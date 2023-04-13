n = int(input())
r = int(input())
s = list(map(int, input().split()))
result = {}
for i in range(r):
    if s[i] in result:
        result[s[i]][0] += 1
    else:
        if len(result) < n:
            result[s[i]] = [1, i]
        else:
            temp = sorted(result.items(), key=lambda x: (x[1],x[0]))
            result.pop(temp[0][0])
            result[s[i]] = [1, i]

print(' '.join(map(str, sorted(result.keys()))))