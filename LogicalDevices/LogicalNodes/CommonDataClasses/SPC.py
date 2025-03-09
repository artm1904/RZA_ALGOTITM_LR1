from dataclasses import dataclass, field
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.BasicTypes.BOOLEAN import BOOLEAN
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.Enum.CtlModels import CtlModels
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.Quality import Quality
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.TimeStamp import TimeStamp


@dataclass
class SPC:
    """
    Представляет Single Point Status (Статус единичной точки).
    """
    ctlVal: Optional[BOOLEAN] = field(default_factory=BOOLEAN)  # ctlVal: Значение управления (булево)
    stVal: Optional[BOOLEAN] = field(default_factory=BOOLEAN)  # stVal: Значение статуса (булево)
    q: Quality = field(default_factory=Quality)                             # q: Качество
    t: TimeStamp = field(default_factory=TimeStamp)                        # t: Временная меткаefault_factory=TimeStam
    ctlModel: Optional[CtlModels] = field(default_factory=CtlModels)