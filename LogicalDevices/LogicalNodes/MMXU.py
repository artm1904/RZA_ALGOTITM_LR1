from dataclasses import field
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.SAV import SAV
from LogicalDevices.LogicalNodes.CommonDataClasses.WYE import WYE
from LogicalDevices.LogicalNodes.Fourier import Fourier
from LogicalDevices.LogicalNodes.LogicalNodeClass import LogicalNodeClass


class MMXU(LogicalNodeClass):
    """
      LN: Measurement Name: MMXU (LN: Название измерения: MMXU)

      Получать значения от CTs и VTs и вычислять измеряемые величины, такие как среднеквадратичные значения
      тока и напряжения или потоки мощности из полученных выборок напряжения и тока. Эти значения обычно
      используются для оперативных целей, таких как контроль и управление потоком мощности, отображение
      на экране, оценка состояния и т.д. Должна быть обеспечена требуемая точность для этих функций.
      (61850-5 - IEC: 2013)

      Функциональный класс LN: LN MMXU
      Процедуры измерения в устройствах защиты являются частью специального алгоритма защиты,
      представленного логическими узлами Xyz. Алгоритмы защиты, как и любая функция, выходят за рамки
      стандарта связи. Поэтому LN Mxyz не должен использоваться в качестве входных данных для Pxyz.
      Данные, связанные с неисправностью, такие как пиковое значение неисправности и т.д.,
      всегда предоставляются строками типа Xyz, а не заимствованиями типа Xyz.
    """

    """
    Входные данные узла:
     """
    CurrentA: Optional[SAV] = field(default_factory=SAV)
    CurrentB: Optional[SAV] = field(default_factory=SAV)
    CurrentC: Optional[SAV] = field(default_factory=SAV)

    """
    Выходные данные узла:
    """
    A: Optional[WYE] = field(default_factory=WYE)

    # Size buffer
    bufSize: int = 80

    # Filter (буферы на каждую фазу)
    ia: Fourier = Fourier(bufSize)
    ib: Fourier = Fourier(bufSize)
    ic: Fourier = Fourier(bufSize)

    def __init__(self):
        LogicalNodeClass.__init__(self)

    def process(self):
        """
        Processes the input values through the filters.
        """
        self.ia.process(self.CurrentA, self.A.phsA)
        self.ib.process(self.CurrentB, self.A.phsB)
        self.ic.process(self.CurrentC, self.A.phsC)
