from dataclasses import dataclass, field
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.SAV import SAV
from LogicalDevices.LogicalNodes.LogicalNodeClass import LogicalNodeClass

@dataclass
class TCTR(LogicalNodeClass):
    InputAmp: SAV = field(init=False) #Инициализируем в __post_init__
    Amp: Optional[SAV] = field(init=False, default=None) #Инициализируем в __post_init__

    def __post_init__(self):
        self.InputAmp = SAV() # Создаем экземпляр SAV
        self.Amp = SAV()

    def process(self):
        self.Amp = self.InputAmp