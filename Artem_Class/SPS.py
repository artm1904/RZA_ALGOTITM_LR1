from dataclasses import dataclass, field
from typing import Optional

from Artem_Class.AnalogueValue import AnalogueValue
from Artem_Class.Quality import Quality
from Artem_Class.TimeStamp import TimeStamp
from LogicalDevices.LogicalNodes.CompositeCommonDataClasses.SimpleCommonDataClasses.CommonDATypes.CompositeComponents.PrimitiveComponents.BasicTypes.BOOLEAN import \
    BOOLEAN


@dataclass
class SPS:
    """
    Представляет Single Point Status (Статус единичной точки).
    """
    stVal: Optional[BOOLEAN] = field(default_factory=BOOLEAN)  # stVal: Значение статуса (булево)
    q: Quality = field(default_factory=Quality)                             # q: Качество
    t: TimeStamp = field(default_factory=TimeStamp)                           # t: Временная меткаefault_factory=TimeStam