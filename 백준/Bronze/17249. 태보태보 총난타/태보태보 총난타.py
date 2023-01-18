s = input()

f_l = s.find('(')
f_r = s.find(')')
print(s[:f_l].count('@'), s[f_r:].count('@'))