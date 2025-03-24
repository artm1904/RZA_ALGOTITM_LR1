from dataclasses import dataclass, field
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.ACD import ACD
from LogicalDevices.LogicalNodes.CommonDataClasses.ACT import ACT
from LogicalDevices.LogicalNodes.CommonDataClasses.ASG import ASG
from LogicalDevices.LogicalNodes.CommonDataClasses.ING import ING
from LogicalDevices.LogicalNodes.CommonDataClasses.WYE import WYE
from LogicalDevices.LogicalNodes.PTOC import PTOC
from LogicalDevices.LogicalNodes.PTRC import PTRC

@dataclass
class LDProt_MTZ:

    """ Входные данные LD """
    A: WYE = field(init=False)

    StrVal_stg1: ASG = field(init=False)
    StrVal_stg2: ASG = field(init=False)
    StrVal_stg3: ASG = field(init=False)

    OPDlTmms_stg1: ING = field(init=False)
    OPDlTmms_stg2: ING = field(init=False)
    OPDlTmms_stg3: ING = field(init=False)

    """ Выходные данные LD """
    Op: ACT = field(init=False)
    Str: ACD = field(init=False)

    """ Экземпляры LN """
    ptoc1: PTOC = field(init=False)
    ptoc2: PTOC = field(init=False)
    ptoc3: PTOC = field(init=False)
    ptrc: PTRC = field(init=False)

    def __post_init__(self):
        self.A = WYE()
        self.StrVal_stg1 = ASG()
        self.StrVal_stg2 = ASG()
        self.StrVal_stg3 = ASG()
        self.OPDlTmms_stg1 = ING()
        self.OPDlTmms_stg2 = ING()
        self.OPDlTmms_stg3 = ING()
        self.Op = ACT()
        self.ptoc1 = PTOC()
        self.ptoc2 = PTOC()
        self.ptoc3 = PTOC()
        self.ptrc = PTRC()



    def process(self):

        # Передача значения уставок
        self.ptoc1.StrVal = self.StrVal_stg1
        self.ptoc2.StrVal = self.StrVal_stg2
        self.ptoc3.StrVal = self.StrVal_stg3

        # Передача значения времени
        self.ptoc1.OpDlTmms = self.OPDlTmms_stg1
        self.ptoc2.OpDlTmms = self.OPDlTmms_stg2
        self.ptoc3.OpDlTmms = self.OPDlTmms_stg3

        # Передача измеренных значений
        self.ptoc1.A = self.A
        self.ptoc2.A = self.A
        self.ptoc3.A = self.A

        self.ptoc1.process()
        self.ptoc2.process()
        self.ptoc3.process()

        # Передача сигналов пусков защит
        self.ptrc.Str1 = self.ptoc1.Str
        self.ptrc.Str2 = self.ptoc2.Str
        self.ptrc.Str3 = self.ptoc3.Str

        # Передача сигналов срабатывания защит
        self.ptrc.Op1 = self.ptoc1.Op
        self.ptrc.Op2 = self.ptoc2.Op
        self.ptrc.Op3 = self.ptoc3.Op

        self.ptrc.process()

        # Передача выходного сигнала срабатывания защит
        self.Op = self.ptrc.Op
        self.Str = self.ptrc.Str