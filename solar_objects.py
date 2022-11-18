# coding: utf-8
# license: GPLv3


class Body:
    """Тип данных, описывающий небесное тело.
    Содержит массу, координаты, скорость тела,
    а также визуальный радиус тела в пикселах и его цвет.
    """

    def __init__(self, type="na", m=1, x=0, y=0, Vx=0, Vy=0, R=5, color="red", image=None):

        self.type = type
        """Признак объекта. Принимает значения "Star", "Planet" и "NA"."""

        self.m = m
        """Масса тела"""

        self.x = x
        """Координата по оси **x**"""

        self.y = y
        """Координата по оси **y**"""

        self.Vx = Vx
        """Скорость по оси **x**"""

        self.Vy = Vy
        """Скорость по оси **y**"""

        self.Fx = 0
        """Сила по оси **x**"""

        self.Fy = 0
        """Сила по оси **y**"""

        self.R = R
        """Радиус тела"""

        self.color = color
        """Цвет тела"""

        self.image = None
        """Изображение тела"""

    def draw(self, screen):
        pass    # FIXME