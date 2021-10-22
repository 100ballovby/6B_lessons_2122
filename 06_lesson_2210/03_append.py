array = []  # пустой список

print(array)
# .append(x) - добавить элемент x в список
array.append('Добавил')
print(array)

# Цикличное наполнение списка
marks = []
for mark in range(1, 11):  # повторить 10 раз
    m = int(input(f'Введите оценку {mark}: '))
    # получаю оценки и сохраняю в список:
    marks.append(m)

print(marks)

