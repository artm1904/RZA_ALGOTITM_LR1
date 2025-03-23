from dataclasses import dataclass, field
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.BasicTypes.BOOLEAN import BOOLEAN
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.Enum.QPosEnum import QPosEnum
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.Quality import Quality
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.TimeStamp import TimeStamp


@dataclass
class DPC:


    """
     Controllable double point (Управляемая двойная точка)
    	Status and control mirror
    """
    stVal: Optional[QPosEnum] = field(default_factory=lambda: QPosEnum("off"))  # stVal: Значение статуса (булево)

    q: Quality = field(default_factory=Quality)          # q: Качество
    t: TimeStamp = field(default_factory=TimeStamp)      # t: Временная меткаefault_factory=TimeStam
    ctlVal: Optional[BOOLEAN] = field(default_factory=lambda: BOOLEAN(False)) # Если BOOLEAN - класс обертка