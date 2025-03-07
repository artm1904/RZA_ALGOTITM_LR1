from dataclasses import dataclass, field
from email.policy import default
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.BasicTypes.INT24U import INT24U
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.BasicTypes.INT32 import INT32
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.TimeQuality import TimeQuality


@dataclass
class TimeStamp:
    """
    Представляет временную метку.
    """
    SecondSinceEpoch: Optional[INT32] = field(default_factory=INT32)  # SecondSinceEpoch: INT32
    FractionOfSecond: Optional[INT24U] = field(default_factory=INT24U)  # FractionOfSecond: INT24U
    TimeQuality: Optional[TimeQuality] = field(default_factory=TimeQuality)    # TimeQuality: TimeQuality,
