from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.ENC import ENC
from LogicalDevices.LogicalNodes.CommonDataClasses.ENS import ENS
from LogicalDevices.LogicalNodes.CommonDataClasses.LPL import LPL


@dataclass
# Создаем абстрактный класс
class LogicalNodeClass(ABC):

    Mod: Optional[ENC] = field(default_factory=ENC)
    Beh: Optional[ENS] = field(default_factory=ENS)
    Health: Optional[ENS] = field(default_factory=ENS)
    NamPlt: Optional[LPL] = field(default_factory=LPL)



    @abstractmethod
    def process(self):
        pass

