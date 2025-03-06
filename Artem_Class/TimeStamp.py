from dataclasses import dataclass, field
from typing import Optional

from Artem_Class.TimeQuality import TimeQuality
from LogicalDevices.LogicalNodes.CompositeCommonDataClasses.SimpleCommonDataClasses.CommonDATypes.CompositeComponents.PrimitiveComponents.BasicTypes.INT24U import \
    INT24U
from LogicalDevices.LogicalNodes.CompositeCommonDataClasses.SimpleCommonDataClasses.CommonDATypes.CompositeComponents.PrimitiveComponents.BasicTypes.INT32 import \
    INT32


@dataclass
class TimeStamp:
    """
    Представляет временную метку.
    """
    SecondSinceEpoch: Optional[INT32] = field(default_factory=INT32)  # SecondSinceEpoch: INT32
    FractionOfSecond: Optional[INT24U] = field(default_factory=INT24U)  # FractionOfSecond: INT24U
    TimeQualitys: Optional[TimeQuality] = None    # TimeQuality: TimeQuality,
