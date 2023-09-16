import re, math

def operate(oct_num1, oct_num2, operator):
    dec_num1 = int(oct_num1, 8)
    dec_num2 = int(oct_num2, 8)

    if operator == '+':
        result = dec_num1 + dec_num2
    elif operator == '-':
        result = dec_num1 - dec_num2
    elif operator == '*':
        result = dec_num1 * dec_num2
    elif operator == '/':
        if dec_num2 == 0:
            return "invalid"
        else:
            result = math.floor(dec_num1 / dec_num2)

    return result


input_str = input()
pattern = re.compile(r"(-?\d+)(\+|-|\*|/)(-?\d+)")
matched = pattern.match(input_str)
num1, operator, num2 = matched.groups()


result = operate(num1, num2, operator)
if type(result) == type('str'):
    pass 
elif result < 0:
    result = oct(result)[0]+oct(result)[3:]
else:
    result = oct(result)[2:]
print(result)
