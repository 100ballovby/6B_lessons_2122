number = input('Введите трехзначное число: ')
# ^ строчку можно итерировать
mult = 1

for digit in number:  # для каждой цифры в строке (str) number
    d = int(digit)
    print(f'{mult} * {d} = {mult * d}')
    mult *= d
