from itertools import product

V = ['A','E','I','O','U']
words = []
for i in range(1, 6):
    for j in product(V, repeat=i):
        words.append(''.join(j))
words.sort()

def solution(word):
    answer = words.index(word)+1
    return answer