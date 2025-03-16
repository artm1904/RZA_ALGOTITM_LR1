from dataclasses import field
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.ACT import ACT
from LogicalDevices.LogicalNodes.CommonDataClasses.ASG import ASG
from LogicalDevices.LogicalNodes.CommonDataClasses.ING import ING
from LogicalDevices.LogicalNodes.CommonDataClasses.WYE import WYE
from LogicalDevices.LogicalNodes.PTOC import PTOC
from LogicalDevices.LogicalNodes.PTRC import PTRC


class LDProt_MTZ:

    """ Входные данные LD """
    A: Optional[WYE] = field(default_factory=WYE)

    StrVal_stg1: Optional[ASG] = field(default_factory=ASG)
    StrVal_stg2: Optional[ASG] = field(default_factory=ASG)
    StrVal_stg3: Optional[ASG] = field(default_factory=ASG)

    OPDlTmms_stg1: Optional[ING] = field(default_factory=ING)
    OPDlTmms_stg2: Optional[ING] = field(default_factory=ING)
    OPDlTmms_stg3: Optional[ING] = field(default_factory=ING)

    """ Выходные данные LD """
    Op: Optional[ACT] = None

    """ Экземпляры LN """
    ptoc1 = PTOC()
    ptoc2 = PTOC()
    ptoc3 = PTOC()
    ptrc = PTRC()


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



