age = int(input('Сколько тебе лет? '))

if age <= 5:  # основное условие
    print('Low')
elif age < 18:  # ИНАЧЕ если
    print('Medium')
elif age < 30:
    print('Medi-medium')
else:  # иначе
    print('High')

