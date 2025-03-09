from dataclasses import dataclass, field
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.BasicTypes.INT32 import INT32
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.Enum.CtlModels import CtlModels
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.Quality import Quality
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.TimeStamp import TimeStamp


@dataclass
class INC:
    """
    Целочисленное управление и состояние
    """
    stVal: Optional[INT32] = field(default_factory=INT32)  # stVal: Значение статуса (булево)
    q: Quality = field(default_factory=Quality)                  # q: Качество
    t: TimeStamp = field(default_factory=TimeStamp)          # t: Временная меткаefault_factory=TimeStam
    ctIModel: CtlModels = field(default_factory=CtlModels)