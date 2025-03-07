from dataclasses import dataclass, field
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.Enum.QPosEnum import QPosEnum
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.Quality import Quality
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.TimeStamp import TimeStamp
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.BasicTypes.BOOLEAN import BOOLEAN


@dataclass
class DPC:


    """
     Controllable double point (Управляемая двойная точка)
    	Status and control mirror
    """
    stVal: Optional[QPosEnum] = field(default_factory=QPosEnum.value)  # stVal: Значение статуса (булево)

    q: Quality = field(default_factory=Quality)          # q: Качество
    t: TimeStamp = field(default_factory=TimeStamp)      # t: Временная меткаefault_factory=TimeStam
    ctlVal: Optional[BOOLEAN] = field(default_factory=BOOLEAN)
