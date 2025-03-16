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

    A: Optional[WYE] = field(default_factory=WYE)

    StrVal: Optional[ASG] = field(default_factory=ASG)
    OpDlTmms: Optional[ING] = field(default_factory=ING)

    Str: Optional[ACD] = None
    Op: Optional[ACT] = None

    def __init__(self):
        super().__init__()

    def process(self):
        StrPhsA = self.A.phsA.cVal.mag.i.value >= self.StrVal.setMag.i.value
        StrPhsB = self.A.phsB.cVal.mag.i.value >= self.StrVal.setMag.i.value
        StrPhsC = self.A.phsC.cVal.mag.i.value >= self.StrVal.setMag.i.value
        StrLoc = (StrPhsA) or (StrPhsB) or (StrPhsC)
        counter = 0

        if StrLoc:
            self.Str = ACD(
                        general=BOOLEAN(True),
                        phsA=BOOLEAN(StrPhsA),
                        phsB=BOOLEAN(StrPhsB),
                        phsC=BOOLEAN(StrPhsC),
                        neut=BOOLEAN(False),
                        dirGeneral=DirEnum.UNKNOWN,
                        dirPhsA=DirEnum.UNKNOWN,
                        dirPhsB=DirEnum.UNKNOWN,
                        dirPhsC=DirEnum.UNKNOWN,
                        dirNeut=DirEnum.UNKNOWN,
                        q=Quality(),
                        t=TimeStamp()
                        )
            counter += 1
            if counter >= self.OpDlTmms.setVal.value:
                self.Op = ACT(
                        general=BOOLEAN(True),
                        phsA=BOOLEAN(StrPhsA),
                        phsB=BOOLEAN(StrPhsB),
                        phsC=BOOLEAN(StrPhsC),
                        neut=BOOLEAN(False),
                        q=Quality(),
                        t=TimeStamp()
                )
        else:
            counter = 0

