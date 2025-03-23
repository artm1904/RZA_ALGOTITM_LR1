from dataclasses import dataclass, field
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.BasicTypes.INT24U import INT24U
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.BasicTypes.INT32 import INT32
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.TimeQuality import TimeQuality

@dataclass
class TimeStamp:
    """
    Представляет временную метку.
    """
    SecondSinceEpoch: INT32 = field(init=False)
    FractionOfSecond: INT24U = field(init=False)
    TimeQuality: TimeQuality = field(init=False)

    def __post_init__(self):
        self.SecondSinceEpoch = INT32(0)
        self.FractionOfSecond = INT24U(0)
        self.TimeQuality = TimeQuality()