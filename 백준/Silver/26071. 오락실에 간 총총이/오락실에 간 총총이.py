import sys
input = sys.stdin.readline

n = int(input())
i_d = []
j_d = []
i_min = j_min = n
i_max = j_max = 0
for i in range(n):
    x = input()
    for j in range(n):
        if x[j] == 'G':
            i_d.append(i)
            j_d.append(j)
i_min = min(i_d)
i_max = max(i_d)
j_min = min(j_d)
j_max = max(j_d)
if (i_min == i_max) and (j_min == j_max):
    r = 0
elif (i_min == i_max):
    r = min(j_max, n-1-j_min)
elif (j_min == j_max):
    r = min(i_max, n-1-i_min)
else:
    r = min(j_max, n-1-j_min) + min(i_max, n-1-i_min)
print(r)