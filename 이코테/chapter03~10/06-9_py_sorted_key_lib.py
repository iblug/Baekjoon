array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting, reverse=True)
print(result)

array.sort(key=lambda x : (x[0], x[1])) # '-'부호를 이용해서 역순으로 가능
print(array)