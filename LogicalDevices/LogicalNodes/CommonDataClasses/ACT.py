from dataclasses import dataclass, field
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.BasicTypes.BOOLEAN import BOOLEAN
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.Quality import Quality
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.TimeStamp import TimeStamp


@dataclass
class ACT:
    """
    Представляет объект ACT.
    """
    general: Optional[BOOLEAN] = field(default_factory=BOOLEAN)    # general: BOOLEAN
    phsA: Optional[BOOLEAN] = field(default_factory=BOOLEAN)        # phSA: BOOLEAN
    phsB: Optional[BOOLEAN] = field(default_factory=BOOLEAN)         # phSB: BOOLEAN
    phsC: Optional[BOOLEAN] = field(default_factory=BOOLEAN)      # phSC: BOOLEAN
    neut: Optional[BOOLEAN] = field(default_factory=BOOLEAN)        # neut: BOOLEAN
    q: Quality = field(default_factory=Quality)          # q: Качество
    t: TimeStamp = field(default_factory=TimeStamp)      # t: Временная меткаefault_factory=TimeStam