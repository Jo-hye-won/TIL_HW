arr = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]
result = sorted(arr, key=setting)
print(result)
