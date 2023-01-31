n = int(input())
[print(('*'*i).rjust(n)) for i in range(n, 0, -1)]