import numpy as np
from typing import List
from solar_objects import SpaceObject
from solar_vis import DrawableObject


class World:
    def __init__(self) -> None:
        """
        perform_execution Флаг цикличности выполнения расчёта

        model_time Физическое время от начала расчёта.
        Тип: float

        time_scale
        Шаг по времени при моделировании.
        Тип: float

        space_objects
        Список космических объектов

        scale_factor
        Масштабирование экранных координат по отношению к физическим.
        Тип: float
        Мера: количество пикселей на один метр

        graph_time
        Массив значений времени для построения графиков

        graph_speed
        Массив значений скорости спутника в каждый момент времени

        graph_S
        Массив значений расстояния от планеты до спутника в каждый момент времени
        Масштабирование экранных координат по отношению к физическим.

        scale_factor
        Тип: float
        Мера: количество пикселей на один метр.
        """
        self.alive = True
        self.perform_execution = False
        self.model_time = 0
        self.time_scale = 100000.0
        self.space_objects = []
        self._drawable_objects = []
        self.scale_factor = 1.0
        self.graph_time = np.array([])
        self.graph_speed = np.array([])
        self.graph_S = np.array([])
        self.scale_factor=1

    @property
    def drawable_objects(self) -> List[DrawableObject]:
        return self._drawable_objects

    @drawable_objects.setter
    def drawable_objects(self, value: List[SpaceObject]) -> None:
        self._drawable_objects = [DrawableObject(obj) for obj in value]

    def __repr__(self) -> str:
        return (
            f"alive: {self.alive}, perform_execution: {self.perform_execution}, model_time: {self.model_time}, "
            + "time_scale: {self.time_scale}, space_objects: {self.space_objects}, scale_factor: {self.scale_factor}, "
            + "graph_time: {self.graph_time}, graph_speed: {self.graph_speed}, graph_S: {self.graph_S}"
        )
