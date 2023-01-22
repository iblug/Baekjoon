d=set(input() for _ in range(int(input())))
print(*sorted(d,key=lambda x:(len(x),x)),sep='\n')