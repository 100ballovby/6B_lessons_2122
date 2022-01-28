"""
Метод pop удаляет из списка.
1) .pop() - удалить последний элемент из списка
2) .pop(index) - удалить элемент с порядковым номером index
"""

my_food = ['pizza', 'chips', 'grape',
           'sushi', 'burger']
print(my_food)
my_food.pop()  # удаляю последний элемент
print(my_food)

print(f'Третий элемент списка: {my_food[2]}')
# списки поддерживают индексацию.
# У каждого элемента списка есть порядковый номер.

print('Убираю чипсики')
my_food.pop(1)  # удаляю элемент с индексом 1 (чипсы)
print(my_food)
