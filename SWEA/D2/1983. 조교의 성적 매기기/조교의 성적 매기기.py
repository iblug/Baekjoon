s = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(n)]

    d_ = [(i[0]*35 + i[1]*45 + i[2]*20)/100 for i in d]

    target = d_[k-1]
    d_ = sorted(d_,reverse=True)
    rank = d_.index(target) + 1
    g = -(-rank//(n//10)) - 1

    print(f'#{t+1}', s[g])