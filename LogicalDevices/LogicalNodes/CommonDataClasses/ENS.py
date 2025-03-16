from dataclasses import dataclass, field
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.BasicTypes.BOOLEAN import BOOLEAN


@dataclass
class ENS:
    """
    Представляет состояние узла.
    """
    stVal: Optional[BOOLEAN] = field(default_factory=BOOLEAN)  # stVal: Значение статуса (булево)