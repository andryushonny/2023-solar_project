# coding: utf-8
# license: GPLv3


class SpaceObject:
    """Тип данных, описывающий объект.
    Содержит массу, координаты, скорость объекта,
    а также визуальный радиус объекта в пикселах и её цвет.
    """


    def __init__(self, type, m = 1, x = 0, y = 0, v_x = 0, v_y = 0, f_x = 0, f_y = 0, R = 5, color = "white"):
        """self.type Признак объекта star или planet, self.m Масса объекта, self.x Координата по оси **x**, 
        self.y Координата по оси **y**, self.Vx Скорость по оси **x**, self.Vy  Скорость по оси **y**
        self.Fx Сила по оси **x**, self.Fy Сила по оси **y**, self.R Радиус объекта, 
        self.color Цвет объекта, self.alive Существование объекта"""
        self.type = type  # Признак объекта star или planet
        self.m = m  # Масса объекта
        self.x = x  # Координата по оси **x**
        self.y = y  # Координата по оси **y**
        self.Vx = v_x  # Скорость по оси **x**
        self.Vy = v_y  # Скорость по оси **y**
        self.Fx = f_x  # Сила по оси **x**
        self.Fy = f_y  # Сила по оси **y**
        self.R = R  # Радиус объекта
        self.color = color  # Цвет объекта
        self.alive = 1  # Существование объекта


if __name__ == "__main__":
    print("This module is not for direct call!")
