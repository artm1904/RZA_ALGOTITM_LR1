from dataclasses import dataclass, field

from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.Quality import Quality
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.TimeStamp import TimeStamp
from LogicalDevices.LogicalNodes.CommonDataClasses.Vector import Vector


@dataclass
class CMV:
    cVal: Vector = field(default_factory=Vector)
    q: Quality = field(default_factory=Quality)          # q: Качество
    t: TimeStamp = field(default_factory=TimeStamp)      # t: Временная меткаefault_factory=TimeStam