from dataclasses import dataclass, field
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.BasicTypes.BOOLEAN import BOOLEAN
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.Enum.dirEnum import DirEnum
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.Quality import Quality
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.TimeStamp import TimeStamp

@dataclass
class ACD:
    """
    Представляет объект ACD.
    """
    general: BOOLEAN = field(init=False)
    dirGeneral: DirEnum = field(default=DirEnum.UNKNOWN, init=False)
    phsA: BOOLEAN = field(init=False)
    dirPhsA: DirEnum = field(default=DirEnum.UNKNOWN, init=False)
    phsB: BOOLEAN = field(init=False)
    dirPhsB: DirEnum = field(default=DirEnum.UNKNOWN, init=False)
    phsC: BOOLEAN = field(init=False)
    dirPhsC: DirEnum = field(default=DirEnum.UNKNOWN, init=False)
    neut: BOOLEAN = field(init=False)
    dirNeut: DirEnum = field(default=DirEnum.UNKNOWN, init=False)
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