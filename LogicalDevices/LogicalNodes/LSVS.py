from dataclasses import field, dataclass
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.SAV import SAV
from LogicalDevices.LogicalNodes.LogicalNodeClass import LogicalNodeClass

@dataclass
class LSVS(LogicalNodeClass):



    def process(self):
        self.CurrentA = self.InputCurrentA
        self.CurrentB = self.InputCurrentB
        self.CurrentC = self.InputCurrentC


    InputCurrentA: Optional[SAV] = field(default_factory=SAV)
    InputCurrentB: Optional[SAV] = field(default_factory=SAV)
    InputCurrentC: Optional[SAV] = field(default_factory=SAV)

    CurrentA: Optional[SAV] = field(init=False, default_factory=SAV) # init=False
    CurrentB: Optional[SAV] = field(init=False, default_factory=SAV) # init=False
    CurrentC: Optional[SAV] = field(init=False, default_factory=SAV) # init=False


