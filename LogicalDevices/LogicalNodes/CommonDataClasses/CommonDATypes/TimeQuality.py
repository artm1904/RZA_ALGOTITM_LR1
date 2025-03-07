from dataclasses import dataclass, field
from typing import Optional

from LogicalDevices.LogicalNodes.CompositeCommonDataClasses.SimpleCommonDataClasses.CommonDATypes.BasicTypes.BOOLEAN import \
    BOOLEAN

from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.Enum.TimeAccuracy import TimeAccuracy


@dataclass
class TimeQuality:
    """
    Представляет качество временной метки.
    """
    LeapSecondsKnown: Optional[BOOLEAN] = field(default_factory=BOOLEAN) # LeapSecondsKnown: BOOLEAN
    ClockFailure: Optional[BOOLEAN] = field(default_factory=BOOLEAN)      # ClockFailure: BOOLEAN
    TimeAccuracys: Optional[TimeAccuracy] = None # TimeAccuracy: CODED ENUM

