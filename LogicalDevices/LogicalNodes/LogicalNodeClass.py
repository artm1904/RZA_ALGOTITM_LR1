from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.INC import INC
from LogicalDevices.LogicalNodes.CommonDataClasses.INS import INS
from LogicalDevices.LogicalNodes.CommonDataClasses.LPL import LPL
from LogicalDevices.LogicalNodes.CommonDataClasses.SAV import SAV


@dataclass
# Создаем абстрактный класс
class LogicalNodeClass(ABC):

    Mod: Optional[INC] = field(default_factory=INC)
    Beh: Optional[INS] = field(default_factory=INS)
    Health: Optional[INS] = field(default_factory=INS)
    NamPlt: Optional[LPL] = field(default_factory=LPL)

    InputCurrentA: Optional[SAV] = field(default_factory=SAV)
    InputCurrentB: Optional[SAV] = field(default_factory=SAV)
    InputCurrentC: Optional[SAV] = field(default_factory=SAV)

    CurrentA: Optional[SAV] = field(default_factory=SAV)
    CurrentB: Optional[SAV] = field(default_factory=SAV)
    CurrentC: Optional[SAV] = field(default_factory=SAV)

    @abstractmethod
    def process(self):
        self.CurrentA = self.InputCurrentA
        self.CurrentB = self.InputCurrentB
        self.CurrentC = self.InputCurrentC
