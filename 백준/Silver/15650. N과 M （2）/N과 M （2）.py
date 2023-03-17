def com(arr, r):
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen):
        if len(chosen) == r:
            print(' '.join(chosen))
            return
        
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for i in range(start, len(arr)):
            if not used[i] and (i == 0 or arr[i-1] != arr[i]):
                used[i] = 1
                chosen.append(arr[i])
                generate(chosen)
                used[i] = 0
                chosen.pop()
    generate([])

            
N, M = map(int, input().split())
d = map(str,range(1, N+1))
com(d, M)