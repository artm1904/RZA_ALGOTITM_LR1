from dataclasses import dataclass, field
from typing import Optional

from Artem_Class.Quality import Quality
from Artem_Class.TimeStamp import TimeStamp
from Data_Class.Enum.QPosEnum import QPosEnum
from LogicalDevices.LogicalNodes.CompositeCommonDataClasses.SimpleCommonDataClasses.CommonDATypes.CompositeComponents.PrimitiveComponents.BasicTypes.BOOLEAN import \
    BOOLEAN


@dataclass
class DPC:


    """
     Controllable double point (Управляемая двойная точка)
    	Status and control mirror
    """
    stVal: Optional[QPosEnum] = field(default_factory=QPosEnum)  # stVal: Значение статуса (булево)

    q: Quality = field(default_factory=Quality)          # q: Качество
    t: TimeStamp = field(default_factory=TimeStamp)      # t: Временная меткаefault_factory=TimeStam
    ctlVal: Optional[BOOLEAN] = field(default_factory=BOOLEAN)
