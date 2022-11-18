# coding: utf-8
# license: GPLv3

from solar_objects import Body
from solar_vis import DrawableObject


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    bodies = []
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            body = Body()
            parse_body_parameters(line, body)
            bodies.append(body)

    return [DrawableObject(obj) for obj in bodies]


def parse_body_parameters(line, body):  # parse_planet_parameters
    """Считывает данные о теле из строки.
    Входная строка должна иметь слеюущий формат:

    <тип тела> <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты тела, (Vx, Vy) — скорость;
    тип тела принимает значения "star", "planet", "NA"

    Пример строки:

    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание тела.

    **body** — объект тела.
    """
    args = line.split()
    body.type = args[0].lower()
    body.R = int(args[1])
    body.color = args[2]
    body.m = int(args[3])
    body.x, body.y, body.Vx, body.Vy = int(args[4]), int(args[5]), int(args[6]), int(args[7])
    # FIXME: не понимает экспоненциальную запись


def write_space_objects_data_to_file(output_filename, objects):
    """Сохраняет данные о космических объектах в файл.

    Строки должны иметь следующий формат:

    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла

    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in objects:
            print(out_file, "%s %d %s %f %f %f %f %f" % (obj.type.capitalize(), obj.R, obj.color,
                                                         obj.m, obj.x, obj.y, obj.Vx, obj.Vy))


if __name__ == "__main__":
    print("This module is not for direct call!")
