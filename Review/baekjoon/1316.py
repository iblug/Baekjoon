# https://www.acmicpc.net/problem/1316
# 그룹 단어 체커
n = int(input())

def group_word(word):
    data = [0 for _ in range(26)]
    pre = word[0]
    now_index = ord(pre) - ord('a')
    data[now_index] = 1
    for now in word:
        now_index = ord(now) - ord('a')
        if now !=  pre:
            if data[now_index] == 1:
                return False
            else:
                data[now_index] = 1
                pre = now
    return True

count = 0

for i in range(n):
    word = input()
    if group_word(word) == True:
        count += 1
print(count)

# 억지로 끼워맞추기
# 완전 다르게 접근했다!
# 
#########################################################3
# 슬라이싱 활용


########################################################
# sorted