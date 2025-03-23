from dataclasses import field
from typing import Optional

from LogicalDevices.LogicalNodes.CSWI import CSWI
from LogicalDevices.LogicalNodes.CommonDataClasses.ACT import ACT
from LogicalDevices.LogicalNodes.CommonDataClasses.DPC import DPC
from LogicalDevices.LogicalNodes.XCBR import XCBR


class LDCtrl:
    """
    Входные данные LD:
     """
    Op: Optional[ACT] = field(default_factory=ACT)

    """
    Выходные данные LD:
    """
    Pos: Optional[DPC] = None

    cswi = CSWI()
    xcbr = XCBR()

    def process(self):
        self.cswi.Op = self.Op
        self.cswi.process()

        self.xcbr.Pos = self.cswi.Pos
        self.xcbr.process()

        self.Pos = self.xcbr.Pos