import sys
input = sys.stdin.readline

while ((n := float(input())) > 0) :
    print(f'Objects weighing {round(n,3):.2f} on Earth will weigh {round(n*0.167, 3):.2f} on the moon.')