from dataclasses import field, dataclass
import functools
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.CMV import CMV
from LogicalDevices.LogicalNodes.CommonDataClasses.SAV import SAV
from LogicalDevices.LogicalNodes.CommonDataClasses.WYE import WYE
from LogicalDevices.LogicalNodes.Fourier import Fourier
from LogicalDevices.LogicalNodes.LogicalNodeClass import LogicalNodeClass

@dataclass
class MMXU_Fur(LogicalNodeClass):
    """
      LN: Measurement Name: MMXU (LN: Название измерения: MMXU)

      ... (описание класса) ...
    """

    """
    Входные данные узла:
     """
    CurrentA: SAV = field(init=False) # init=False
    CurrentB: SAV = field(init=False) # init=False
    CurrentC: SAV = field(init=False) # init=False

    """
    Выходные данные узла:
    """
    A: WYE = field(init=False)  # init=False - т.к. присваивается в process

    # Size buffer
    bufSize: int = 80

    # Filter (буферы на каждую фазу)
    ia: Fourier = field(init=False)
    ib: Fourier = field(init=False)
    ic: Fourier = field(init=False)

    def __post_init__(self):
        self.A = WYE()  # Инициализация A
        self.CurrentA = SAV() # Инициализация CurrentA
        self.CurrentB = SAV() # Инициализация CurrentB
        self.CurrentC = SAV() # Инициализация CurrentC
        self.ia = Fourier(self.bufSize)
        self.ib = Fourier(self.bufSize)
        self.ic = Fourier(self.bufSize)

    def process(self):
        """
        Processes the input values through the filters.
        """
        magnitude_a, angle_a = self.ia.process(self.CurrentA)
        magnitude_b, angle_b = self.ib.process(self.CurrentB)
        magnitude_c, angle_c = self.ic.process(self.CurrentC)

        self.A.phsA = CMV() # Создаем экземпляр CMV для phsA
        self.A.phsA.cVal.mag.f.value = magnitude_a # Устанавливаем значения
        self.A.phsA.cVal.ang.f.value = angle_a

        self.A.phsB = CMV() # Создаем экземпляр CMV для phsB
        self.A.phsB.cVal.mag.f.value = magnitude_b # Устанавливаем значения
        self.A.phsB.cVal.ang.f.value = angle_b

        self.A.phsC = CMV() # Создаем экземпляр CMV для phsC
        self.A.phsC.cVal.mag.f.value = magnitude_c # Устанавливаем значения
        self.A.phsC.cVal.ang.f.value = angle_c



@dataclass
class MMXU_RMS(LogicalNodeClass):
    """
      LN: Measurement Name: MMXU (LN: Название измерения: MMXU)

 и управление потоком мощности, отображение
      на экране, оценка состояния и т.д. Должна быть обеспечена требуемая точность для этих функций.
      (61850-5 - IEC: 2013)

      Функциональный класс LN: LN M входных данных для Pxyz.
      Данные, связанные с неисправностью, такие как пиковое значение неисправности и т.д.,
      всегда предоставляются строками типа Xyz, а не заимствованиями типа Xyz.
    """

    """
    Входные данные узла:
     """
    CurrentA: SAV = field(init=False)
    CurrentB: SAV = field(init=False)
    CurrentC: SAV = field(init=False)

    """
    Выходные данные узла:
    """
    A: WYE = field(init=False) # init=False - т.к. присваивается в process

    # Size buffer
    bufSize: int = 80

    # Filter (буферы на каждую фазу)
    ia: Fourier = field(init=False)
    ib: Fourier = field(init=False)
    ic: Fourier = field(init=False)



    def __post_init__(self):
        self.A = WYE() # Инициализация A
        self.ia = Fourier(self.bufSize)
        self.ib = Fourier(self.bufSize)
        self.ic = Fourier(self.bufSize)

    def process(self):
        """
        Processes the input values through the filters.
        """
        magnitude_a, angle_a = self.ia.process(self.CurrentA)
        magnitude_b, angle_b = self.ib.process(self.CurrentB)
        magnitude_c, angle_c = self.ic.process(self.CurrentC)

        self.A.phsA = CMV() # Создаем экземпляр CMV для phsA
        self.A.phsA.cVal.mag.f.value = magnitude_a # Устанавливаем значения
        self.A.phsA.cVal.ang.f.value = angle_a

        self.A.phsB = CMV() # Создаем экземпляр CMV для phsB
        self.A.phsB.cVal.mag.f.value = magnitude_b # Устанавливаем значения
        self.A.phsB.cVal.ang.f.value = angle_b

        self.A.phsC = CMV() # Создаем экземпляр CMV для phsC
        self.A.phsC.cVal.mag.f.value = magnitude_c # Устанавливаем значения
        self.A.phsC.cVal.ang.f.value = angle_c