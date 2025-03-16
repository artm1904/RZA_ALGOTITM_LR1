from dataclasses import field
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.SAV import SAV
from LogicalDevices.LogicalNodes.CommonDataClasses.WYE import WYE
from LogicalDevices.LogicalNodes.LSVS import LSVS
from LogicalDevices.LogicalNodes.MMXU import MMXU_Fur, MMXU_RMS
from LogicalDevices.LogicalNodes.TCTR import TCTR


class LDMeasurement_LSVS_Fur:
    """
    Входные данные LD:
     """
    CurrentA: Optional[SAV] = field(default_factory=SAV)
    CurrentB: Optional[SAV] = field(default_factory=SAV)
    CurrentC: Optional[SAV] = field(default_factory=SAV)

    """
    Выходные данные LD:
    """
    A: Optional[WYE] = None

    mmxu = MMXU_Fur()
    lsvs = LSVS()

    def process(self):
        self.lsvs.InputCurrentA = self.CurrentA
        self.lsvs.InputCurrentB = self.CurrentB
        self.lsvs.InputCurrentC = self.CurrentC
        self.lsvs.process()

        self.mmxu.CurrentA = self.lsvs.CurrentA
        self.mmxu.CurrentB = self.lsvs.CurrentB
        self.mmxu.CurrentC = self.lsvs.CurrentC
        self.mmxu.process()
        self.A = self.mmxu.A

class LDMeasurement_TCTR_Fur:
    """
    Входные данные LD:
     """
    CurrentA: Optional[SAV] = field(default_factory=SAV)
    CurrentB: Optional[SAV] = field(default_factory=SAV)
    CurrentC: Optional[SAV] = field(default_factory=SAV)

    """
    Выходные данные LD:
    """
    A: Optional[WYE] = None

    mmxu = MMXU_Fur()
    tctrA = TCTR()
    tctrB = TCTR()
    tctrC = TCTR()

    def process(self):
        self.tctrA.InputAmp = self.CurrentA
        self.tctrB.InputAmp = self.CurrentB
        self.tctrC.InputAmp = self.CurrentC

        self.tctrA.process()
        self.tctrB.process()
        self.tctrC.process()

        self.mmxu.CurrentA = self.tctrA.Amp
        self.mmxu.CurrentB = self.tctrB.Amp
        self.mmxu.CurrentC = self.tctrC.Amp
        self.mmxu.process()
        self.A = self.mmxu.A


class LDMeasurement_LSVS_RMS:
    """
    Входные данные LD:
     """
    CurrentA: Optional[SAV] = field(default_factory=SAV)
    CurrentB: Optional[SAV] = field(default_factory=SAV)
    CurrentC: Optional[SAV] = field(default_factory=SAV)

    """
    Выходные данные LD:
    """
    A: Optional[WYE] = None

    mmxu = MMXU_RMS()
    lsvs = LSVS()

    def process(self):
        self.lsvs.InputCurrentA = self.CurrentA
        self.lsvs.InputCurrentB = self.CurrentB
        self.lsvs.InputCurrentC = self.CurrentC
        self.lsvs.process()

        self.mmxu.CurrentA = self.lsvs.CurrentA
        self.mmxu.CurrentB = self.lsvs.CurrentB
        self.mmxu.CurrentC = self.lsvs.CurrentC
        self.mmxu.process()
        self.A = self.mmxu.A


class LDMeasurement_TCTR_RMS:
    """
    Входные данные LD:
     """
    CurrentA: Optional[SAV] = field(default_factory=SAV)
    CurrentB: Optional[SAV] = field(default_factory=SAV)
    CurrentC: Optional[SAV] = field(default_factory=SAV)

    """
    Выходные данные LD:
    """
    A: Optional[WYE] = None

    mmxu = MMXU_RMS()
    tctrA = TCTR()
    tctrB = TCTR()
    tctrC = TCTR()

    def process(self):
        self.tctrA.InputAmp = self.CurrentA
        self.tctrB.InputAmp = self.CurrentB
        self.tctrC.InputAmp = self.CurrentC

        self.tctrA.process()
        self.tctrB.process()
        self.tctrC.process()

        self.mmxu.CurrentA = self.tctrA.Amp
        self.mmxu.CurrentB = self.tctrB.Amp
        self.mmxu.CurrentC = self.tctrC.Amp
        self.mmxu.process()
        self.A = self.mmxu.A