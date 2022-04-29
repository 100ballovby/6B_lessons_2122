filename = 'pi_digits.txt'  # сохраняю имя файла в переменной

with open(filename) as file:
    # открыть файл и записать его в переменную
    print(file.read())  # прочитать файл и распечатать его содержимое
