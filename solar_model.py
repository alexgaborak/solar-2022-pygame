# coding: utf-8
# license: GPLv3

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.

    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        x = obj.x - body.x
        y = obj.y - body.y
        r = (x ** 2 + y ** 2) ** 0.5
        if r == 0:
            continue
        f = gravitational_constant * obj.m * body.m / r ** 2
        body.Fx += f * x / r
        body.Fy += f * y / r


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """
    ax = body.Fx / body.m
    body.x += body.Vx * dt + ax * dt ** 2 / 2
    body.Vx += ax * dt
    ay = body.Fy / body.m
    body.y += body.Vy * dt + ay * dt ** 2 / 2
    body.Vy += ay * dt


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.

    **dt** — шаг по времени
    """
    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
