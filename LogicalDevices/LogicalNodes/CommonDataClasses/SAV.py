from dataclasses import dataclass, field

from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.AnalogueValue import AnalogueValue
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.Quality import Quality
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.TimeStamp import TimeStamp


@dataclass
class SAV:
    """
    Представляет Single Analogue Value (Единичное аналоговое значение).
    """
    instMag: AnalogueValue = field(default_factory=AnalogueValue)  # instMag: Мгновенная величина
    q: Quality = field(default_factory=Quality)                             # q: Качество
    t: TimeStamp = field(default_factory=TimeStamp)                           # t: Временная метка