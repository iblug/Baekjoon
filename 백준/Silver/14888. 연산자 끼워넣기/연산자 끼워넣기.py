def per(t, l):
    if l == n-1:
        r.append(t)
        return
    
    for i in range(4):
        if o[i]:
            o[i] -= 1
            if i == 0:
                per(t + a[l+1],l+1)
            elif i == 1:
                per(t - a[l+1],l+1)
            elif i == 2:
                per(t * a[l+1],l+1)
            else:
                if t < 0:
                    per(-(-t // a[l+1]),l+1)
                else:
                    per(t // a[l+1],l+1)
            o[i] += 1


n = int(input())
a = list(map(int, input().split()))
o = list(map(int, input().split()))
r = []
per(a[0],0)
print(max(r), min(r), sep='\n')