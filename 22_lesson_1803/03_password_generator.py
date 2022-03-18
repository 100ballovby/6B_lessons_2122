import random as r
import string as s


def generate_password(count, length):
    """
    Функция генерирует пользователю случайные пароли
    :param count: количество паролей
    :param length: длина каждого пароля
    :return: список с паролями
    """
    my_passwords = []
    alphabet = s.ascii_letters + s.digits  # строка
    # алфавит для паролей - все буквы английского алфавита + цифры
    for i in range(count):  # делаю необходимое количество паролей
        password = ''  # создаю пустую строку для пароля
        for passw in range(length):  # повторить [длина пароля] раз
            password += r.choice(alphabet)  # добавить случайный символ из алфавита
        my_passwords.append(password)  # добавить готовый пароль в список паролей
    return my_passwords  # вернуть список паролей


print(generate_password(10, 8))


