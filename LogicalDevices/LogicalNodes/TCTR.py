from dataclasses import field
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.INS import INS
from LogicalDevices.LogicalNodes.CommonDataClasses.SAV import SAV
from LogicalDevices.LogicalNodes.LogicalNodeClass import LogicalNodeClass


class TCTR(LogicalNodeClass):

    EEHealth: Optional[INS] = field(default_factory=INS)    # EEHealth: INS
    Amp: Optional[SAV] = field(default_factory=SAV)           # Amp: SAV


    InputCurrentA: Optional[SAV] = field(default_factory=SAV)
    InputCurrentB: Optional[SAV] = field(default_factory=SAV)
    InputCurrentC: Optional[SAV] = field(default_factory=SAV)

    CurrentA: Optional[SAV] = field(default_factory=SAV)
    CurrentB: Optional[SAV] = field(default_factory=SAV)
    CurrentC: Optional[SAV] = field(default_factory=SAV)
    def __init__(self):
        LogicalNodeClass.__init__(self)

    def process(self):
        self.CurrentA = self.InputCurrentA
        self.CurrentB = self.InputCurrentB
        self.CurrentC = self.InputCurrentC


