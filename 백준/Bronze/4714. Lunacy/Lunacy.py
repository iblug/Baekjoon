import sys
input = sys.stdin.readline

while ((n := float(input())) > 0) :
    print(f'Objects weighing {n:.2f} on Earth will weigh {n*0.167:.2f} on the moon.')