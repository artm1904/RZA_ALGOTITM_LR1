from dataclasses import field
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.SAV import SAV
from LogicalDevices.LogicalNodes.LogicalNodeClass import LogicalNodeClass


class TVTR(LogicalNodeClass):

    InputVol: Optional[SAV] = field(default_factory=SAV)
    Vol: Optional[SAV] = None  # Vol: SAV

    def __init__(self):
        LogicalNodeClass.__init__(self)

    def process(self):
        self.Vol = self.InputVol

