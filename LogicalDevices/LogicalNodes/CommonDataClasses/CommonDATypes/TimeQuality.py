from dataclasses import dataclass, field
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.BasicTypes.BOOLEAN import BOOLEAN
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.Enum.TimeAccuracy import TimeAccuracy


@dataclass
class TimeQuality:
    """
    Представляет качество временной метки.
    """
    LeapSecondsKnown: Optional[BOOLEAN] = field(default_factory=BOOLEAN) # LeapSecondsKnown: BOOLEAN
    ClockFailure: Optional[BOOLEAN] = field(default_factory=BOOLEAN)      # ClockFailure: BOOLEAN
    TimeAccuracy: Optional[TimeAccuracy] = TimeAccuracy.T_0_01 # TimeAccuracy: CODED ENUM

