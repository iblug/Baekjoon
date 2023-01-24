def find_(x,arr, end, start):
    if start > end:
        return None
    mid = (end + start) // 2
    if x == arr[mid]:
        return mid
    if x < arr[mid]:
        return find_(x, arr, mid-1, start)
    elif x > arr[mid]:
        return find_(x, arr, end, mid + 1)
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a.sort()
for b1 in b:
    result = find_(b1, a, n - 1, 0)
    if result == None:
        print(0)
    else:
        print(1)