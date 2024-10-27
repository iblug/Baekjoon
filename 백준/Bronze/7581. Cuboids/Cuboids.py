import sys
input = sys.stdin.readline

while 1:
    l, w, h, v = map(int, input().split())
    if l or w or h or v:
        if not l:
            print(v//(h*w), w, h, v)
        elif not w:
            print(l, v//(h*l), h, v)
        elif not h:
            print(l, w, v//(l*w), v)
        elif not v:
            print(l, w, h, l*w*h)
    else:
        break
