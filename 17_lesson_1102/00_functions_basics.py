def function():  # это функция
    txt = 'Hello!'
    return txt


def procedure():  # это процедура
    print('Hello!')


a = function()
b = procedure()

print(a[5])  # достать элемент с индексом 5
print(b[5])  # из пустой переменной нельзя достать элемент с индексом 5 
