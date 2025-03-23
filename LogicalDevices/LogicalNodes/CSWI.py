from dataclasses import dataclass, field
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.ACT import ACT
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.Quality import Quality
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.TimeStamp import TimeStamp
from LogicalDevices.LogicalNodes.CommonDataClasses.DPC import DPC
from LogicalDevices.LogicalNodes.LogicalNodeClass import LogicalNodeClass

"""
Логический узел «Оперативное управление коммутационным аппаратом»

Данный логический узел используется для управления всеми состояниями переключений выше технологического уровня. Логический узел
должен выполнить подписку на получение данных POWCap — point-on-wave switching capability (фаза точки
переключения) от узла XCBR, если это возможно. 

Функции, моделируемые логическим узлом CSWI:
1) Режим работы логического узла;
2) Отображение статуса места управления;
3) Управление местом управления;
4) Выдача статуса управления;
5) Управление КА.

Применяется один экземпляр ЛУ на один КА.
"""


@dataclass
class CSWI(LogicalNodeClass):

    """ Входные данные """
    Op: Optional[ACT] = field(default_factory=ACT)

    """ Выходные данные """
    Pos: Optional[DPC] = None

    def process(self):
        self.Pos = DPC(
            stVal = True,
            q=Quality(),
            t=TimeStamp(),
            ctlVal= True
        )