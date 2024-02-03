n = int(input())
k = int(input())
answer = n * 1500
if n > k+60:
    answer += (n - (k+60)) * 1500
print(answer)