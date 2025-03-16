from dataclasses import dataclass, field
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.ACD import ACD
from LogicalDevices.LogicalNodes.CommonDataClasses.ACT import ACT
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.BasicTypes.BOOLEAN import BOOLEAN
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.Enum.dirEnum import DirEnum
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.Quality import Quality
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.TimeStamp import TimeStamp
from LogicalDevices.LogicalNodes.LogicalNodeClass import LogicalNodeClass


"""
Логический узел «Общий сигнал срабатывания защит»

Данный логический узел (LN) используется для соединения выходов operate одной или нескольких
защитных функций в общий выход trip, чтобы выдать команду отключения на узел XCBR.

Функции, моделируемые логическим узлом PTRC:
1) Режим работы логического узла;
2) Пуск и срабатывание функции.


Op - Срабатывать (тип атрибута ACT класса общих данных) — означает решение функции защиты (логического узла) об отключении.
Команда на отключение выдается в узле PTRC

Узел PTRC используется для того, чтобы соединять и поддерживать состояние различных
сигналов, направленных на отключение, в единое состояние отключения.

Все сигналы срабатывания, идущие от узлов защиты, объединяются в команду на отключение в узле PTRC.
Узел PTRC контролирует создание условий для сигнала отключения (минимальная продолжительность команды на отключение, однополюсный/трехполюсный вариант и т. п.).
"""

@dataclass
class PTRC(LogicalNodeClass):
    """
        Входные данные узла:
         """
    Str1: Optional[ACD] = field(default_factory=ACD)
    Str2: Optional[ACD] = field(default_factory=ACD)
    Str3: Optional[ACD] = field(default_factory=ACD)

    Op1: Optional[ACT] = field(default_factory=ACT)
    Op2: Optional[ACT] = field(default_factory=ACT)
    Op3: Optional[ACT] = field(default_factory=ACT)

    """
        Выходные данные узла:
        """
    Str: Optional[ACD] = None
    Op: Optional[ACT] = None


    def __init__(self):
        super().__init__()

    def process(self):

        if ( (self.Op1.phsA) or (self.Op2.phsA) or (self.Op3.phsA)):
            StrPhsA = True

        if ( (self.Op1.phsB) or (self.Op2.phsB) or (self.Op3.phsB)):
            StrPhsB = True

        if ( (self.Op1.phsC) or (self.Op2.phsC) or (self.Op3.phsC)):
            StrPhsC = True


        StrLoc = (StrPhsA) or (StrPhsB) or (StrPhsC)


        if StrLoc:
            self.Str = ACD(
                general=BOOLEAN(True),
                phsA=BOOLEAN(StrPhsA),
                phsB=BOOLEAN(StrPhsB),
                phsC=BOOLEAN(StrPhsC),
                neut=BOOLEAN(False),
                dirGeneral=DirEnum.UNKNOWN,
                dirPhsA=DirEnum.UNKNOWN,
                dirPhsB=DirEnum.UNKNOWN,
                dirPhsC=DirEnum.UNKNOWN,
                dirNeut=DirEnum.UNKNOWN,
                q=Quality(),
                t=TimeStamp()
            )
            self.Op = ACT(
                    general=BOOLEAN(True),
                    phsA=BOOLEAN(StrPhsA),
                    phsB=BOOLEAN(StrPhsB),
                    phsC=BOOLEAN(StrPhsC),
                    neut=BOOLEAN(False),
                    q=Quality(),
                    t=TimeStamp()
            )