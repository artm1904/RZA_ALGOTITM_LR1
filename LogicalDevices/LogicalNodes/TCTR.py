from dataclasses import field
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.INS import INS
from LogicalDevices.LogicalNodes.CommonDataClasses.SAV import SAV
from LogicalDevices.LogicalNodes.LogicalNodeClass import LogicalNodeClass


class TCTR(LogicalNodeClass):

    InputAmp: Optional[SAV] = field(default_factory=SAV)
    Amp: Optional[SAV] = None             # Amp: SAV



    def __init__(self):
        LogicalNodeClass.__init__(self)

    def process(self):
        self.Amp = self.InputAmp


