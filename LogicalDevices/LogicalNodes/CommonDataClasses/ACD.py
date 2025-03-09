from dataclasses import dataclass, field
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.Quality import Quality
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.TimeStamp import TimeStamp
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.Enum.dirEnum import DirEnum
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.BasicTypes.BOOLEAN import BOOLEAN


@dataclass
class ACD:

    """
    Представляет объект ACD.
           /**
    * Directional protection activation information
    * (Информация об активации направленной защиты)
    * */
    /**
    * Status
    */
        """
    general: Optional[BOOLEAN] = field(default_factory=BOOLEAN)     # general: BOOLEAN
    dirGeneral: Optional[DirEnum] = field(default_factory=DirEnum)   # dirGeneral: ENUMERATED

    phsA: Optional[BOOLEAN] = field(default_factory=BOOLEAN)         # phSA: BOOLEAN
    dirPhsA: Optional[DirEnum] = field(default_factory=DirEnum)     # dirPhSA: ENUMERATED

    phsB: Optional[BOOLEAN] = field(default_factory=BOOLEAN)          # phSB: BOOLEAN
    dirPhsB: Optional[DirEnum] = field(default_factory=DirEnum)     # dirPhSB: ENUMERATED

    phsC: Optional[BOOLEAN] = field(default_factory=BOOLEAN)           # phSC: BOOLEAN
    dirPhsC: Optional[DirEnum] = field(default_factory=DirEnum)     # dirPhSC: ENUMERATED

    neut: Optional[BOOLEAN] = field(default_factory=BOOLEAN)            # neut: BOOLEAN
    dirNeut: Optional[DirEnum] = field(default_factory=DirEnum)     # dirNeut: ENUMERATED

    q: Quality = field(default_factory=Quality)          # q: Качество
    t: TimeStamp = field(default_factory=TimeStamp)      # t: Временная меткаefault_factory=TimeStam

