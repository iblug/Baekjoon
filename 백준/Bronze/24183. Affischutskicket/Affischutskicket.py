w_c4, w_a3, w_a4 = map(int, input().split())
s_c4 = 0.229 * 0.324
s_a3 = 0.297 * 0.420
s_a4 = 0.210 * 0.297

p_c4 = w_c4*s_c4
p_a3 = w_a3*s_a3
p_a4 = w_a4*s_a4

print(p_c4 * 2 + p_a3 * 2 + p_a4)