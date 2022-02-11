def draw_square(turt, x, y, col, line):
    """
    Процедура будет рисовать квадрат с заданными парметрами
    :param turt: черепашка (кто рисует)
    :param x: координаты квадрата
    :param y: координаты квадрата
    :param col: цвет
    :param line: длина стороны
    :return: None (ничего не возвращает)
    """
    turt.up()
    turt.goto(x, y)
    turt.color(col)
    turt.down()
    for i in range(4):
        turt.fd(line)
        turt.rt(90)
    turt.up()