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
"""

@dataclass
class PTRC(LogicalNodeClass):
    """
        Входные данные узла:
         """
    Str1: ACD = field(init=False)
    Str2: ACD = field(init=False)
    Str3: ACD = field(init=False)

    Op1: ACT = field(init=False)
    Op2: ACT = field(init=False)
    Op3: ACT = field(init=False)

    """
        Выходные данные узла:
         """
    Str: ACD = field(init=False)
    Op: ACT = field(init=False)

    def __post_init__(self):
        self.Str1 = ACD()
        self.Str2 = ACD()
        self.Str3 = ACD()
        self.Op1 = ACT()
        self.Op2 = ACT()
        self.Op3 = ACT()
        self.Str = ACD()
        self.Op = ACT()

    def process(self):
        StrPhsA = False
        StrPhsB = False
        StrPhsC = False

        if ( (self.Op1.phsA.value) or (self.Op2.phsA.value) or (self.Op3.phsA.value)):
            StrPhsA = True

        if ( (self.Op1.phsB.value) or (self.Op2.phsB.value) or (self.Op3.phsB.value)):
            StrPhsB = True

        if ( (self.Op1.phsC.value) or (self.Op2.phsC.value) or (self.Op3.phsC.value)):
            StrPhsC = True


        StrLoc = (StrPhsA) or (StrPhsB) or (StrPhsC)


        if StrLoc:
            self.Str = ACD()
            self.Str.general = BOOLEAN(True)
            self.Str.phsA = BOOLEAN(StrPhsA)
            self.Str.phsB = BOOLEAN(StrPhsB)
            self.Str.phsC = BOOLEAN(StrPhsC)
            self.Str.neut = BOOLEAN(False)
            self.Str.dirGeneral = DirEnum.UNKNOWN
            self.Str.dirPhsA = DirEnum.UNKNOWN
            self.Str.dirPhsB = DirEnum.UNKNOWN
            self.Str.dirPhsC = DirEnum.UNKNOWN
            self.Str.dirNeut = DirEnum.UNKNOWN
            self.Str.q = Quality()
            self.Str.t = TimeStamp()


            self.Op = ACT()
            self.Op.general = BOOLEAN(True)
            self.Op.phsA = BOOLEAN(StrPhsA)
            self.Op.phsB = BOOLEAN(StrPhsB)
            self.Op.phsC = BOOLEAN(StrPhsC)
            self.Op.neut = BOOLEAN(False)
            self.Op.q = Quality()
            self.Op.t = TimeStamp()