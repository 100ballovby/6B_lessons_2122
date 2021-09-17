'''
Строкой в программировании называется абсолютно любая
последовательность символов, заключенная в кавычки.
'''
name = 'Демид'  # создал строчную переменную
l_name = 'Раксин'

print(name)  # вывел ее

'''
Со строчками можно выполнять мат.операции:
+ строчки можно складывать !!! str + str !!!  "a" + "b" = "ab"
* строчки можно умножать !!! str * int !!! "a" * 5 = "aaaaa"
🔪 строчки можно разрезать
'''
print(name + l_name)  # конкатенация
print(name * 3)

'''
Т.к. строка - это последовательно, у каждого члена этой последовательности
есть свой порядковый номер. Называется он индекс. 
Индексы в строке начинаются с 0
'''

phrase = 'Привет! Я разработчик!'
# если нужно обратиться к определенному индексу:
print(phrase[4])


