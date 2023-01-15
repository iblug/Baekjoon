while True:
    n=input()
    if n=='0':
        break
    print('yneos'[n!=n[::-1]::2])