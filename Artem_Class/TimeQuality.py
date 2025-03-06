from dataclasses import dataclass, field
from typing import Optional

from Data_Class.Enum.TimeAccuracy import TimeAccuracy
from LogicalDevices.LogicalNodes.CompositeCommonDataClasses.SimpleCommonDataClasses.CommonDATypes.CompositeComponents.PrimitiveComponents.BasicTypes.BOOLEAN import \
    BOOLEAN


@dataclass
class TimeQuality:
    """
    Представляет качество временной метки.
    """
    LeapSecondsKnown: Optional[BOOLEAN] = field(default_factory=BOOLEAN) # LeapSecondsKnown: BOOLEAN
    ClockFailure: Optional[BOOLEAN] = field(default_factory=BOOLEAN)      # ClockFailure: BOOLEAN
    TimeAccuracys: Optional[TimeAccuracy] = None # TimeAccuracy: CODED ENUM

