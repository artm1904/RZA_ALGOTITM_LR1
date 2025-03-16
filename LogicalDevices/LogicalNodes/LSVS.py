from dataclasses import field
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.SAV import SAV
from LogicalDevices.LogicalNodes.LogicalNodeClass import LogicalNodeClass


class LSVS(LogicalNodeClass):

    def __init__(self):
        LogicalNodeClass.__init__()

    def process(self):
        self.CurrentA = self.InputCurrentA
        self.CurrentB = self.InputCurrentB
        self.CurrentC = self.InputCurrentC


    InputCurrentA: Optional[SAV] = field(default_factory=SAV)
    InputCurrentB: Optional[SAV] = field(default_factory=SAV)
    InputCurrentC: Optional[SAV] = field(default_factory=SAV)

    CurrentA: Optional[SAV] = field(default_factory=SAV)
    CurrentB: Optional[SAV] = field(default_factory=SAV)
    CurrentC: Optional[SAV] = field(default_factory=SAV)


