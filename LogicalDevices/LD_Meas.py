from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from LogicalDevices.LogicalNodes.CommonDataClasses.SAV import SAV
from LogicalDevices.LogicalNodes.CommonDataClasses.WYE import WYE
from LogicalDevices.LogicalNodes.LSVS import LSVS
from LogicalDevices.LogicalNodes.MMXU import MMXU_Fur, MMXU_RMS
from LogicalDevices.LogicalNodes.TCTR import TCTR

# Абсстрактный класс используется в качестве интерфейса
class LD_Meas(ABC):
    """
        Входные данные LD:
         """
    CurrentA: SAV = field(init=False)
    CurrentB: SAV = field(init=False)
    CurrentC: SAV = field(init=False)

    """
    Выходные данные LD:
    """
    A: WYE = field(init=False)

    @abstractmethod
    def process(self):
        pass

@dataclass
class LDMeasurement_LSVS_Fur(LD_Meas):

    mmxu: MMXU_Fur = field(init=False)
    lsvs: LSVS = field(init=False)

    def __post_init__(self):
        self.mmxu = MMXU_Fur()
        self.lsvs = LSVS()
        self.CurrentA = SAV()
        self.CurrentB = SAV()
        self.CurrentC = SAV()
        self.A = WYE()

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


@dataclass
class LDMeasurement_TCTR_Fur(LD_Meas):
    mmxu: MMXU_Fur = field(init=False)
    tctrA: TCTR = field(init=False)
    tctrB: TCTR = field(init=False)
    tctrC: TCTR = field(init=False)

    def __post_init__(self):
        self.mmxu = MMXU_Fur()
        self.tctrA = TCTR()
        self.tctrB = TCTR()
        self.tctrC = TCTR()
        self.CurrentA = SAV()
        self.CurrentB = SAV()
        self.CurrentC = SAV()
        self.A = WYE()

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



@dataclass
class LDMeasurement_LSVS_RMS(LD_Meas):
    mmxu: MMXU_RMS = field(init=False)
    lsvs: LSVS = field(init=False)

    def __post_init__(self):
        self.mmxu = MMXU_RMS()
        self.lsvs = LSVS()
        self.CurrentA = SAV()
        self.CurrentB = SAV()
        self.CurrentC = SAV()
        self.A = WYE()

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


@dataclass
class LDMeasurement_TCTR_RMS(LD_Meas):

    mmxu: MMXU_RMS = field(init=False)
    tctrA: TCTR = field(init=False)
    tctrB: TCTR = field(init=False)
    tctrC: TCTR = field(init=False)

    def __post_init__(self):
        self.mmxu = MMXU_RMS()
        self.tctrA = TCTR()
        self.tctrB = TCTR()
        self.tctrC = TCTR()
        self.CurrentA = SAV()
        self.CurrentB = SAV()
        self.CurrentC = SAV()
        self.A = WYE()

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