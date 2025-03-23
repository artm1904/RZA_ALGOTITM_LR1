from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.BasicTypes.BOOLEAN import BOOLEAN
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.Quality import Quality
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.TimeStamp import TimeStamp

@dataclass
class ACT:
    """
    Представляет объект ACT.
    """
    general: BOOLEAN = field(init=False)
    phsA: BOOLEAN = field(init=False)
    phsB: BOOLEAN = field(init=False)
    phsC: BOOLEAN = field(init=False)
    neut: BOOLEAN = field(init=False)
    q: Quality = field(init=False)
    t: TimeStamp = field(init=False)

    def __post_init__(self):
        self.general = BOOLEAN(False)
        self.phsA = BOOLEAN(False)
        self.phsB = BOOLEAN(False)
        self.phsC = BOOLEAN(False)
        self.neut = BOOLEAN(False)
        self.q = Quality()
        self.t = TimeStamp()