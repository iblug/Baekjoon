import sys
input = sys.stdin.readline

i = 1
while (True):
    if (input().rstrip() == '0'):
        break
    sys.stdout.write(f'Case {i}: Sorting... done!\n')
    i += 1
