'''Электронные часы'''
n = int(input('Сколько минут прошло? '))
hours = n % (60 * 24) // 60
minutes = n % 60

print(f'{hours} ч., {minutes} мин.')

