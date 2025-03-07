from dataclasses import dataclass, field
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.BasicTypes.BOOLEAN import BOOLEAN
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.Quality import Quality
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.TimeStamp import TimeStamp


@dataclass
class SPS:
    """
    Представляет Single Point Status (Статус единичной точки).
    """
    stVal: Optional[BOOLEAN] = field(default_factory=BOOLEAN)  # stVal: Значение статуса (булево)
    q: Quality = field(default_factory=Quality)                             # q: Качество
    t: TimeStamp = field(default_factory=TimeStamp)                           # t: Временная меткаefault_factory=TimeStam