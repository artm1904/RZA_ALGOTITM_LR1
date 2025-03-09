from dataclasses import field
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.INS import INS
from LogicalDevices.LogicalNodes.CommonDataClasses.SAV import SAV
from LogicalDevices.LogicalNodes.LogicalNodeClass import LogicalNodeClass


class TVTR(LogicalNodeClass):


    Vol: Optional[SAV] = field(default_factory=SAV)           # Amp: SAV


    InputVoltageA: Optional[SAV] = field(default_factory=SAV)
    InputVoltageB: Optional[SAV] = field(default_factory=SAV)
    InputVoltageC: Optional[SAV] = field(default_factory=SAV)

    VoltageA: Optional[SAV] = field(default_factory=SAV)
    VoltageB: Optional[SAV] = field(default_factory=SAV)
    VoltageC: Optional[SAV] = field(default_factory=SAV)
    def __init__(self):
        LogicalNodeClass.__init__(self)

    def process(self):
        self.VoltageA = self.InputVoltageA
        self.VoltageB = self.InputVoltageB
        self.VoltageC = self.InputVoltageC

