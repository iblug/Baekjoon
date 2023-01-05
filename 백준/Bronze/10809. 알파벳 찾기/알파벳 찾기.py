s = input()

arr = [-1 for _ in range(26)]

for i in s:
    a_i = ord(i) - 97 # 0
    if arr[a_i] != -1:
        continue
    arr[a_i] = s.index(i)
print(*arr, sep=' ')