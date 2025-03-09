from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.INC import INC
from LogicalDevices.LogicalNodes.CommonDataClasses.INS import INS
from LogicalDevices.LogicalNodes.CommonDataClasses.LPL import LPL


@dataclass
# Создаем абстрактный класс
class LogicalNodeClass(ABC):

    Mod: Optional[INC] = field(default_factory=INC)
    Beh: Optional[INS] = field(default_factory=INS)
    Health: Optional[INS] = field(default_factory=INS)
    NamPlt: Optional[LPL] = field(default_factory=LPL)

    @abstractmethod
    def process(self):
        pass  # Абстрактный метод, который должен быть реализован в дочерних классах




# # Дочерний класс, который реализует абстрактные методы
# class Dog(Animal):
#
#     def make_sound(self):
#         return "Woof!"
#
#     def move(self):
#         return "Running on four legs"
#
#
# # Дочерний класс, который реализует абстрактные методы
# class Bird(Animal):
#
#     def make_sound(self):
#         return "Chirp!"
#
#     def move(self):
#         return "Flying"
#
#
# # Пример использования
# dog = Dog()
# print(dog.make_sound())  # Вывод: Woof!
# print(dog.move())  # Вывод: Running on four legs
#
# bird = Bird()
# print(bird.make_sound())  # Вывод: Chirp!
# print(bird.move())  # Вывод: Flying

# Попытка создать экземпляр абстрактного класса вызовет ошибку
# animal = Animal()  # TypeError: Can't instantiate abstract class Animal with abstract methods make_sound, move