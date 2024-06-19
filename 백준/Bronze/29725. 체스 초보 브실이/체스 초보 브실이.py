import sys
input = sys.stdin.readline

r = 0
for _ in range(8):
    s = input().rstrip()
    for e in s:
        match e:
            case '.' | 'K' | 'k':
                continue
            case 'P':
                r += 1
            case 'p':
                r -= 1
            case 'N' | 'B':
                r += 3
            case 'n' | 'b':
                r -= 3
            case 'R':
                r += 5
            case 'r':
                r -= 5
            case 'Q':
                r += 9
            case 'q':
                r -= 9
print(r)