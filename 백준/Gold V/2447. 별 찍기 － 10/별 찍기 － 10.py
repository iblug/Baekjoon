def draw_stars(n):
    if n==1:
        return ['*']

    stars=draw_stars(n//3)
    r=[]

    for star in stars:
        r.append(star*3)
    for star in stars:
        r.append(star+' '*(n//3)+star)
    for star in stars:
        r.append(star*3)

    return r

n=int(input())
print('\n'.join(draw_stars(n)))