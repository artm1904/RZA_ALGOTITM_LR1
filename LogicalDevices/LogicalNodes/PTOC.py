from dataclasses import field, dataclass
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.ACD import ACD
from LogicalDevices.LogicalNodes.CommonDataClasses.ACT import ACT
from LogicalDevices.LogicalNodes.CommonDataClasses.ASG import ASG
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.BasicTypes.BOOLEAN import BOOLEAN
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.Enum.dirEnum import DirEnum
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.Quality import Quality
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.TimeStamp import TimeStamp
from LogicalDevices.LogicalNodes.CommonDataClasses.ING import ING
from LogicalDevices.LogicalNodes.CommonDataClasses.WYE import WYE
from LogicalDevices.LogicalNodes.LogicalNodeClass import LogicalNodeClass


@dataclass
class PTOC(LogicalNodeClass):
    A: WYE = field(init=False)

    StrVal: ASG = field(init=False)
    OpDlTmms: ING = field(init=False)

    Str: ACD = field(init=False)
    Op: ACT = field(init=False)
    counter = 0

    def __post_init__(self):
        self.A = WYE()
        self.StrVal = ASG()
        self.OpDlTmms = ING()
        self.Str = ACD()
        self.Op = ACT()

    def process(self):
        StrPhsA = self.A.phsA.cVal.mag.f.value >= self.StrVal.setMag.f.value
        StrPhsB = self.A.phsB.cVal.mag.f.value >= self.StrVal.setMag.f.value
        StrPhsC = self.A.phsC.cVal.mag.f.value >= self.StrVal.setMag.f.value
        StrLoc = (StrPhsA) or (StrPhsB) or (StrPhsC)

        if StrLoc:
            self.Str.general = BOOLEAN(True)
            self.Str.phsA = BOOLEAN(StrPhsA)
            self.Str.phsB = BOOLEAN(StrPhsB)
            self.Str.phsC = BOOLEAN(StrPhsC)
            self.Str.neut = BOOLEAN(False)
            self.Str.dirGeneral = DirEnum.UNKNOWN
            self.Str.dirPhsA = DirEnum.UNKNOWN
            self.Str.dirPhsB = DirEnum.UNKNOWN
            self.Str.dirPhsC = DirEnum.UNKNOWN
            self.Str.dirNeut = DirEnum.UNKNOWN
            self.Str.q = Quality()
            self.Str.t = TimeStamp()
            self.counter += 1
            if self.counter >= self.OpDlTmms.setVal.value:
                self.Op.general = BOOLEAN(True)
                self.Op.phsA = BOOLEAN(StrPhsA)
                self.Op.phsB = BOOLEAN(StrPhsB)
                self.Op.phsC = BOOLEAN(StrPhsC)
                self.Op.neut = BOOLEAN(False)
                self.Op.q = Quality()
                self.Op.t = TimeStamp()
        else:
            self.counter = 0
