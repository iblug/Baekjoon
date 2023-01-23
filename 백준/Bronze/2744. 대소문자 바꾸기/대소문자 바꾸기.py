a=input()
r=''
for b in a:
    if b.isupper():
        r+=b.lower()
    else:
        r+=b.upper()
print(r)